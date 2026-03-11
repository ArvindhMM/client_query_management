# Client Query Management System

## Project Overview
The **Client Query Management System** is a Python-based application designed to help organizations manage customer queries efficiently.  
Clients can submit queries, and the support team can track, manage, and resolve those queries through a centralized system.

The project demonstrates database integration, secure authentication using password hashing, and structured backend design.

---

## Features
- Secure login system with **SHA-256 password hashing**
- Role-based access (**Client / Support**)
- Client query submission
- Query tracking and management
- Query status update (**Open / Closed**)
- Timestamp tracking for query creation and closure

---

## Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Backend logic |
| MySQL | Database |
| Streamlit | User interface |
| hashlib | Password hashing |
| mysql-connector-python | Database connection |

---

## Project Structure
``` bash
client-query-management-system
│
├── backend
│ ├── app.py
│ ├── auth.py
│ ├── db.py
│ ├── test_login.py
│
├── data
│ └── dataset.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```


---

## Database Schema

### Users Table

Stores login credentials.

| Column | Description |
|------|-------------|
| username | Login username |
| password | SHA-256 hashed password |
| role | client / support |

Example:
``` bash
Support1
Client1
```


---

### Queries Table

Stores client queries.

| Column | Description |
|------|-------------|
| query_id | Unique query ID |
| mail_id | Client email |
| mobile_number | Phone number |
| query_heading | Query title |
| query_description | Detailed query |
| status | Open / Closed |
| query_created_time | Query creation time |
| query_closed_time | Query resolution time |

---

## Installation Guide

### 1. Clone the Repository
``` bash
git clone https://github.com/your-username/client-query-management-system.git
```
Navigate into the folder:
```bash
cd client-query-management-system
```
---

### 2. Create Virtual Environment
``` bash
python -m venv venv
```
---

### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
---

### 4. Setup MySQL Database

Create database:
``` sql
CREATE DATABASE client_query_management;
```
Create users table:
``` sql
CREATE TABLE users(
username VARCHAR(50),
password VARCHAR(100),
role VARCHAR(20)
);
```
Create queries table:
``` sql
CREATE TABLE queries(
query_id INT AUTO_INCREMENT PRIMARY KEY,
mail_id VARCHAR(100),
mobile_number VARCHAR(20),
query_heading VARCHAR(200),
query_description TEXT,
status VARCHAR(20),
query_created_time DATETIME,
query_closed_time DATETIME
);
```

---

### 5. Update Database Credentials

Edit `db.py`:
``` bash
host="localhost"
user="root"
password="your_mysql_password"
database="client_query_management"
```

---

### 6. Run the Application

Start the backend:
``` bash
python app.py
```
---

## Authentication System

Passwords are stored securely using **SHA-256 hashing**.

Example:

```bash
import hashlib
hashlib.sha256(password.encode()).hexdigest()
```

This ensures that plaintext passwords are never stored in the database.