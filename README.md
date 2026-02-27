🏦 Machine Learning Loan Prediction System

A full-stack web application that predicts the approval status of a bank loan based on an applicant's financial and personal details. The project utilizes a Machine Learning model (Random Forest Classifier) integrated into a Flask backend, with a clean, responsive frontend built using Tailwind CSS.

✨ Features

Machine Learning Integration: Uses a pre-trained scikit-learn model (model.pkl) to instantly predict loan eligibility (Approved/Rejected).

Responsive UI: Modern, mobile-friendly interface built with Tailwind CSS and Lucide Icons.

Engineered Features: Automatically calculates complex ML features (like Total_Income) from basic user inputs.

Support System: Includes a contact form that saves user queries to a local SQLite database.

Containerized: Fully Dockerized for easy deployment and consistent environments.

🛠️ Tech Stack

Frontend: HTML5, Tailwind CSS, JavaScript (Vanilla)

Backend: Python, Flask, Flask-CORS

Machine Learning: Scikit-Learn, Pandas, NumPy

Database: SQLite3

Deployment: Docker, Gunicorn

📂 Project Structure

/
├── app.py                  # Flask backend API & Database setup
├── database_setup.sql      # SQLite schema for user support queries
├── requirements.txt        # Python dependencies
├── model.pkl               # Trained Scikit-Learn ML Model
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Local Docker deployment config
└── templates/              
    └── index.html          # Frontend UI (Served by Flask)


🚀 How to Run Locally (Without Docker)

Prerequisites

Python 3.9+ installed on your machine.

Installation Steps

Clone the repository:

git clone [https://github.com/yourusername/loan-prediction-system.git](https://github.com/yourusername/loan-prediction-system.git)
cd loan-prediction-system


Create a Virtual Environment:

python -m venv venv


Activate the Virtual Environment:

Windows: .\venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install Dependencies:

pip install -r requirements.txt


Run the Application:

python app.py


Note: On the first run, the SQLite database (lps_eightsemproject.db) will be created automatically.

View the App: Open your browser and navigate to http://127.0.0.1:5000

🐳 How to Run Locally (With Docker)

If you have Docker Desktop installed, you can spin up the entire application with one command, without installing Python or any libraries locally.

Open your terminal in the project directory.

Run the Docker Compose build command:

docker-compose up --build


Open your browser and navigate to http://localhost:5000

🌐 Deployment (Render)

This project is configured to be easily deployed on Render using the provided Dockerfile.

Push this repository to GitHub.

Log into Render and click New > Web Service.

Connect your GitHub repository.

Set the Runtime to Docker.

Click Create Web Service.

Render will build the Docker container and provide you with a live URL!

(Note: Render's free tier uses ephemeral storage. The SQLite database will reset if the server sleeps due to inactivity. The ML prediction will always work seamlessly).

📊 Dataset & Model Details

The model was trained on a standardized Loan Prediction dataset containing variables such as:

Gender, Marital Status, Education, Dependents

Applicant Income, Coapplicant Income, Loan Amount, Loan Term

Credit History (The most heavily weighted feature)

Property Area (Urban, Semiurban, Rural)

During data processing, specific categorical variables were One-Hot Encoded. The backend app.py script automatically maps the frontend form inputs back into the exact 13-feature array structure expected by the model.pkl file.
