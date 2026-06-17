````md
# Personal Finance Budget Management System

## Overview

The Personal Finance Budget Management System is a RESTful API built using FastAPI that enables users to manage their personal finances efficiently. The application provides features for user authentication, expense tracking, category management, budget planning, and financial reporting. It uses PostgreSQL as the database backend and JWT-based authentication to ensure secure access to user data.

---

## Features

### User Authentication
- User registration and login
- JWT-based authentication and authorization
- Secure password hashing

### Expense Management
- Add, update, and delete expenses
- Track expenses across different categories
- View expense history

### Category Management
- Create and manage expense categories
- Organize spending records efficiently

### Budget Management
- Create monthly or category-specific budgets
- Monitor spending against budget limits
- Receive insights into budget utilization

### Reporting
- Generate expense summaries
- Analyze spending patterns
- View financial reports and dashboard statistics

---

## Technology Stack

| Component | Technology |
|------------|------------|
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| Authentication | JWT (JSON Web Tokens) |
| Password Security | Argon2 |
| Database Driver | Psycopg2 |
| Environment Management | Python Dotenv |

---

## Project Structure

```text
personal_finance_budget/
│
├── auth.py
├── database.py
├── schemas.py
├── main.py
├── requirements.txt
├── .env
└── README.md
````

### Description

* `main.py` – Application entry point and API routes
* `auth.py` – Authentication and JWT token handling
* `database.py` – Database connection and configuration
* `schemas.py` – Request and response validation models
* `requirements.txt` – Project dependencies
* `.env` – Environment variables and configuration

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/personal-finance-budget.git
cd personal-finance-budget
```

### Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Database Configuration

Create a PostgreSQL database and configure the environment variables in the `.env` file.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/finance_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Running the Application

Start the development server using:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Core API Endpoints

### Authentication

| Method | Endpoint  | Description                                 |
| ------ | --------- | ------------------------------------------- |
| POST   | /register | Register a new user                         |
| POST   | /login    | Authenticate user and generate access token |

### Categories

| Method | Endpoint    |
| ------ | ----------- |
| POST   | /categories |
| GET    | /categories |

### Expenses

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /expenses      |
| GET    | /expenses      |
| PUT    | /expenses/{id} |
| DELETE | /expenses/{id} |

### Budgets

| Method | Endpoint |
| ------ | -------- |
| POST   | /budgets |
| GET    | /budgets |

### Reports

| Method | Endpoint   |
| ------ | ---------- |
| GET    | /reports   |
| GET    | /dashboard |

---

## Security

* JWT-based authentication
* Secure password hashing
* Protected API endpoints
* Environment-based configuration
* Database transaction handling

---

## Future Enhancements

* Export reports to PDF and Excel
* Recurring expense management
* Financial analytics and visualization
* Email notifications and alerts
* Multi-currency support
* Mobile application integration

---

## License

This project is licensed under the MIT License.

---
