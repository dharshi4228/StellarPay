# 🚀 StellarPay – Secure Transaction Management System

## 📌 Overview
**StellarPay** is a high-performance, secure transaction management system built using **Flask**. It simulates a real-world payment gateway environment with a strong focus on **API security, system resilience, and modern UI/UX**.  
The project follows the **Application Factory Pattern** and leverages **Flask Blueprints** to ensure scalability, modularity, and maintainability.

---

## 🛠️ Core Features

### 🔐 Security & Access Control
- **JWT-Based Authentication**  
  Stateless authentication using JSON Web Tokens (JWT) for secure API access.

- **Role-Based Access Control (RBAC)**  
  - **Admin**: Access to audit logs and system monitoring  
  - **User**: Transaction execution and dashboard access  

- **API Rate Limiting**  
  Protects against brute-force attacks and abuse using **Flask-Limiter**.

- **Idempotency Handling**  
  Prevents duplicate transactions by validating unique request identifiers.

---

### ⚙️ Reliability & Resilience
- **Chaos Engineering Module**  
  A toggleable *Chaos Mode* that simulates:
  - Random 5xx server errors  
  - Artificial network latency  
  Used to test frontend and client-side resilience.

- **Structured Logging**  
  Outputs system events in **JSON format**, ready for integration with professional log aggregation tools like the **ELK Stack**.

---

### 🎨 Frontend
- **Modern Fintech Dashboard**  
  - Glassmorphism-style UI  
  - Built using **Tailwind CSS**  
  - Real-time data visualization with **Chart.js**

---

## 🏗️ Technical Stack

### Backend
- Python 3.x  
- Flask  

### Security
- Flask-JWT-Extended  
- Cryptography (AES-256 encryption)

### Database
- SQLAlchemy  
- SQLite (development)

### Frontend
- Tailwind CSS  
- Vanilla JavaScript  
- Chart.js  

### Reliability
- Flask-Limiter (API rate limiting)

---

## 📂 Project Architecture
```text
payment-system/
├── app/
│   ├── __init__.py          # Application Factory & Extension Init
│   ├── models.py            # Database Schema (Encrypted Fields)
│   ├── api/                 # Core Payment Logic Blueprint
│   ├── auth/                # Identity & Access Management Blueprint
│   ├── static/              # Dashboard JS and Charting logic
│   └── templates/           # Jinja2 Dashboard Templates
├── run.py                   # Application Entry Point
├── config.py                # Security & Environment Config
├── .flaskenv                # Flask Environment Variables
└── requirements.txt         # Project Dependencies
```
---
## 🚥 Terminal Commands (Quick Start)

Follow these commands in your **Windows Terminal (PowerShell)** to set up and run the project from scratch.


### Setup

```powershell
# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install required packages
pip install flask flask-sqlalchemy flask-jwt-extended flask-limiter cryptography python-dotenv

# Create the database file and tables
python -c "from app import create_app, db; app=create_app(); app.app_context().push(); db.create_all()"

# Set environment variables
$env:FLASK_APP = "run.py"
$env:FLASK_DEBUG = "1"

# Start the server
flask run
```
