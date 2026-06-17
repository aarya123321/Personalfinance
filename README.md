# Personal Finance Management API

A FastAPI-based backend application for managing personal finances. This API allows users to securely register, authenticate, and manage their financial records such as income, expenses, and budgeting information.

## Features

* User Registration and Authentication
* Secure Password Hashing
* JWT-Based Authentication
* Manage Income Records
* Manage Expense Records
* PostgreSQL Database Integration
* Environment Variable Configuration
* RESTful API Design
* Input Validation using Pydantic

## Tech Stack

* FastAPI
* PostgreSQL
* SQL
* Python
* JWT Authentication
* Passlib (Password Hashing)
* Psycopg2
* Python Dotenv

## Project Structure

```text
PersonalFinance/
│
├── main.py
├── database.py
├── auth.py
├── models.py
├── schemas.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/aarya123321/Personalfinance.git
cd Personalfinance
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/personalfinance
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Run the Application

```bash
uvicorn main:app --reload
```

Application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Example Endpoints

### Authentication

| Method | Endpoint  | Description                 |
| ------ | --------- | --------------------------- |
| POST   | /register | Register a new user         |
| POST   | /login    | Login and receive JWT token |

### Finance Management

| Method | Endpoint           | Description          |
| ------ | ------------------ | -------------------- |
| GET    | /transactions      | Get all transactions |
| POST   | /transactions      | Add transaction      |
| PUT    | /transactions/{id} | Update transaction   |
| DELETE | /transactions/{id} | Delete transaction   |

## Testing

You can test the API using:

* Postman
* Swagger UI
* Thunder Client

## Future Improvements

* Monthly Budget Tracking
* Financial Reports
* Expense Categories
* Data Visualization Dashboard
* Email Notifications
* Multi-user Support

## License

This project is developed for educational and learning purposes.
