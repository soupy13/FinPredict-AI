from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import sqlite3
import pickle
import os

# Initialize Flask App
app = Flask(__name__)
CORS(app)

DB_FILE = 'database.db'
MODEL_FILE = 'model.pkl'

# --- Database Initialization ---
def init_db():
    """Initializes the SQLite database from the SQL file if it doesn't exist."""
    if not os.path.exists(DB_FILE):
        print(f"Initializing database {DB_FILE}...")
        conn = sqlite3.connect(DB_FILE)
        if os.path.exists('database_setup.sql'):
            with open('database_setup.sql', 'r') as f:
                conn.executescript(f.read())
            print("Database initialized successfully.")
        conn.close()

init_db()

# --- Load Machine Learning Model ---
model = None
if os.path.exists(MODEL_FILE):
    with open(MODEL_FILE, 'rb') as f:
        model = pickle.load(f)
    print("Machine Learning Model loaded successfully.")

# --- Routes ---
@app.route('/')
def home():
    """Renders the HTML frontend."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handles Loan Prediction logic."""
    if not model:
        return jsonify({'success': False, 'error': 'Model not loaded.'}), 500

    try:
        data = request.json
        
        # Calculate Engineered Features
        applicant_income = float(data.get('ApplicantIncome', 0))
        coapplicant_income = float(data.get('CoapplicantIncome', 0))
        total_income = applicant_income + coapplicant_income
        
        loan_amount = float(data.get('LoanAmount', 0))
        loan_amount_term = float(data.get('Loan_Amount_Term', 360))
        credit_history = float(data.get('Credit_History', 1))

        # Extract Categorical mappings (One-Hot Encoded)
        is_male = 1 if data.get('Gender') == 'Male' else 0
        is_married = 1 if data.get('Married') == 'Yes' else 0
        dep_1 = 1 if data.get('Dependents') == '1' else 0
        dep_2 = 1 if data.get('Dependents') == '2' else 0
        dep_3plus = 1 if data.get('Dependents') == '3+' else 0
        not_graduate = 1 if data.get('Education') == 'Not Graduate' else 0
        is_self_employed = 1 if data.get('Self_Employed') == 'Yes' else 0
        is_semiurban = 1 if data.get('Property_Area') == 'Semiurban' else 0
        is_urban = 1 if data.get('Property_Area') == 'Urban' else 0

        # Reconstruct the EXACT 13 features expected by your model.pkl
        # We use a list to safely handle the duplicate 'Yes' columns
        feature_values = [[
            loan_amount, loan_amount_term, credit_history, total_income,
            is_male, is_married, dep_1, dep_2, dep_3plus, 
            not_graduate, is_self_employed, is_semiurban, is_urban
        ]]
        
        feature_columns = [
            'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Total_income', 
            'Male', 'Yes', '1', '2', '3+', 
            'Not Graduate', 'Yes', 'Semiurban', 'Urban'
        ]

        df_features = pd.DataFrame(feature_values, columns=feature_columns)

        # Make Prediction
        prediction = model.predict(df_features)[0] 
        is_approved = bool(prediction == 'Y' or prediction == 1)

        return jsonify({'success': True, 'isApproved': is_approved})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/api/contact', methods=['POST'])
def contact_support():
    """Handles saving contact support queries to the database."""
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        contact = data.get('contact')
        message = data.get('message')

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contactsupport (name, email, contact, message, status) 
            VALUES (?, ?, ?, ?, 0)
        ''', (name, email, contact, message))
        
        conn.commit()
        conn.close()
        
        return jsonify({'success': True, 'message': 'Message sent to support successfully!'})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)