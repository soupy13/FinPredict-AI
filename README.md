# 🏦 Machine Learning Loan Prediction System

A full-stack web application that predicts the approval status of a bank loan based on an applicant's financial and personal details. The project utilizes a Machine Learning model (Random Forest Classifier) integrated into a Flask backend, with a clean, responsive frontend built using Tailwind CSS.

## ✨ Features

* **Machine Learning Integration:** Uses a pre-trained `scikit-learn` model (`model.pkl`) to instantly predict loan eligibility (Approved/Rejected).
* **Responsive UI:** Modern, mobile-friendly interface built with Tailwind CSS and Lucide Icons.
* **Engineered Features:** Automatically calculates complex ML features (like `Total_Income`) from basic user inputs.
* **Support System:** Includes a contact form that saves user queries to a local SQLite database.
* **Containerized:** Fully Dockerized for easy deployment and consistent environments.

## 🛠️ Tech Stack

* **Frontend:** HTML5, Tailwind CSS, JavaScript (Vanilla)
* **Backend:** Python, Flask, Flask-CORS
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Database:** SQLite3
* **Deployment:** Docker, Gunicorn

## 📂 Project Structure

```text
/
├── app.py                  # Flask backend API & Database setup
├── database_setup.sql      # SQLite schema for user support queries
├── requirements.txt        # Python dependencies
├── model.pkl               # Trained Scikit-Learn ML Model
├── Dockerfile              # Docker image configuration
├── docker-compose.yml      # Local Docker deployment config
└── templates/              
    └── index.html          # Frontend UI (Served by Flask)
