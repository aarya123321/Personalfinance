## Project Structure

```text
personal_finance_budget/
│
├── app/
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   └── utils.py
│
├── requirements.txt
├── .env.example
├── README.md
└── main.py
```

### Directory Description

| File/Folder        | Description                                           |
| ------------------ | ----------------------------------------------------- |
| `main.py`          | Application entry point and route registration        |
| `app/auth.py`      | Authentication, authorization, and JWT token handling |
| `app/database.py`  | Database connection and configuration                 |
| `app/models.py`    | Database models and table definitions                 |
| `app/schemas.py`   | Request and response validation models                |
| `app/routes/`      | API endpoint implementations                          |
| `app/utils.py`     | Helper and utility functions                          |
| `requirements.txt` | Project dependencies                                  |
| `.env.example`     | Example environment variables                         |
| `README.md`        | Project documentation                                 |

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

## Database Configuration

Create a PostgreSQL database and configure the environment variables in the `.env` file.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/finance_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

## Core API Endpoints

### Authentication

| Method | Endpoint    | Description                                 |
| ------ | ----------- | ------------------------------------------- |
| POST   | `/register` | Register a new user                         |
| POST   | `/login`    | Authenticate user and generate access token |

### Categories

| Method | Endpoint      |
| ------ | ------------- |
| POST   | `/categories` |
| GET    | `/categories` |

### Expenses

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | `/expenses`      |
| GET    | `/expenses`      |
| PUT    | `/expenses/{id}` |
| DELETE | `/expenses/{id}` |

### Budgets

| Method | Endpoint   |
| ------ | ---------- |
| POST   | `/budgets` |
| GET    | `/budgets` |

### Reports

| Method | Endpoint     |
| ------ | ------------ |
| GET    | `/reports`   |
| GET    | `/dashboard` |

## Security

* JWT-based authentication
* Secure password hashing
* Protected API endpoints
* Environment-based configuration
* Database transaction management

## Future Enhancements

* Export reports to PDF and Excel
* Recurring expense management
* Financial analytics and visualization
* Email notifications and alerts
* Multi-currency support
* Mobile application integration

## License

This project is licensed under the MIT License.
