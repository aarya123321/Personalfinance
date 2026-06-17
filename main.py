from datetime import datetime
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from database import get_db, init_db
from auth import create_token, get_current_user, hash_password, verify_password
from schemas import (
    Budget,
    BudgetCreate,
    Category,
    CategoryCreate,
    DashboardResponse,
    Expense,
    ExpenseCreate,
    Login,
    Register,
    Report,
    UserOut,
)

app = FastAPI(title="Personal Finance Budget Management")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    return {
        "message": "Personal Finance Expense Tracking & Budget Management System",
        "description": "FastAPI budgeting platform with JWT authentication, expense tracking, categories, budgets, and reports.",
    }


@app.post("/register", response_model=UserOut)
def register(user: Register, db=Depends(get_db)):
    cur = db.cursor()
    try:
        hashed_password = hash_password(user.password)
        cur.execute(
            "INSERT INTO users (email, password) VALUES (%s, %s) RETURNING id, email",
            (user.email, hashed_password),
        )
        user_id, email = cur.fetchone()
        return {"id": user_id, "email": email}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.post("/login")
def login(user: Login, db=Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT id, password FROM users WHERE email = %s", (user.email,))
    result = cur.fetchone()
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    user_id, hashed_password = result
    if not verify_password(user.password, hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return create_token(user_id)


@app.get("/users/me", response_model=UserOut)
def get_user(user_id: int = Depends(get_current_user), db=Depends(get_db)):
    cur = db.cursor()
    cur.execute("SELECT id, email FROM users WHERE id = %s", (user_id,))
    result = cur.fetchone()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": result[0], "email": result[1]}


@app.post("/categories", response_model=Category)
def create_category(
    category: CategoryCreate,
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO categories (user_id, name) VALUES (%s, %s) RETURNING id, name",
            (user_id, category.name),
        )
        category_id, name = cur.fetchone()
        return {"id": category_id, "name": name}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@app.get("/categories", response_model=List[Category])
def list_categories(
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    cur.execute("SELECT id, name FROM categories WHERE user_id = %s ORDER BY name", (user_id,))
    return [{"id": row[0], "name": row[1]} for row in cur.fetchall()]


@app.post("/expenses", response_model=Expense)
def create_expense(
    expense: ExpenseCreate,
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    cur.execute(
        "INSERT INTO expenses (user_id, category_id, amount, description, spent_at) VALUES (%s, %s, %s, %s, %s) RETURNING id, category_id, amount, description, spent_at, created_at",
        (
            user_id,
            expense.category_id,
            expense.amount,
            expense.description,
            expense.spent_at or datetime.utcnow(),
        ),
    )
    expense_row = cur.fetchone()
    return {
        "id": expense_row[0],
        "category_id": expense_row[1],
        "amount": float(expense_row[2]),
        "description": expense_row[3],
        "spent_at": expense_row[4].isoformat(),
        "created_at": expense_row[5].isoformat(),
    }


@app.get("/expenses", response_model=List[Expense])
def list_expenses(
    category_id: Optional[int] = Query(None),
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    if category_id:
        cur.execute(
            "SELECT id, category_id, amount, description, spent_at, created_at FROM expenses WHERE user_id = %s AND category_id = %s ORDER BY spent_at DESC",
            (user_id, category_id),
        )
    else:
        cur.execute(
            "SELECT id, category_id, amount, description, spent_at, created_at FROM expenses WHERE user_id = %s ORDER BY spent_at DESC",
            (user_id,),
        )
    return [
        {
            "id": row[0],
            "category_id": row[1],
            "amount": float(row[2]),
            "description": row[3],
            "spent_at": row[4].isoformat(),
            "created_at": row[5].isoformat(),
        }
        for row in cur.fetchall()
    ]


@app.post("/budgets", response_model=Budget)
def create_budget(
    budget: BudgetCreate,
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    cur.execute(
        "INSERT INTO budgets (user_id, category_id, monthly_limit, month, year) VALUES (%s, %s, %s, %s, %s) RETURNING id, category_id, monthly_limit, month, year, created_at",
        (user_id, budget.category_id, budget.monthly_limit, budget.month, budget.year),
    )
    row = cur.fetchone()
    return {
        "id": row[0],
        "category_id": row[1],
        "monthly_limit": float(row[2]),
        "month": row[3],
        "year": row[4],
        "created_at": row[5].isoformat(),
    }


@app.get("/budgets", response_model=List[Budget])
def list_budgets(
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    cur.execute(
        "SELECT id, category_id, monthly_limit, month, year, created_at FROM budgets WHERE user_id = %s ORDER BY year DESC, month DESC",
        (user_id,),
    )
    return [
        {
            "id": row[0],
            "category_id": row[1],
            "monthly_limit": float(row[2]),
            "month": row[3],
            "year": row[4],
            "created_at": row[5].isoformat(),
        }
        for row in cur.fetchall()
    ]


@app.get("/reports/monthly", response_model=List[Report])
def monthly_report(
    month: int = Query(..., ge=1, le=12),
    year: int = Query(..., ge=2000),
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    cur.execute(
        "SELECT c.name, SUM(e.amount) FROM expenses e LEFT JOIN categories c ON e.category_id = c.id WHERE e.user_id = %s AND EXTRACT(MONTH FROM e.spent_at) = %s AND EXTRACT(YEAR FROM e.spent_at) = %s GROUP BY c.name ORDER BY SUM(e.amount) DESC",
        (user_id, month, year),
    )
    return [{"category": row[0] or "Uncategorized", "total_spent": float(row[1] or 0)} for row in cur.fetchall()]


@app.get("/dashboard", response_model=DashboardResponse)
def dashboard(
    user_id: int = Depends(get_current_user),
    db=Depends(get_db),
):
    cur = db.cursor()
    cur.execute("SELECT COUNT(*) FROM categories WHERE user_id = %s", (user_id,))
    category_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*), COALESCE(SUM(amount), 0) FROM expenses WHERE user_id = %s", (user_id,))
    expense_count, total_spent = cur.fetchone()

    cur.execute(
        "SELECT month, year, COALESCE(SUM(monthly_limit), 0) FROM budgets WHERE user_id = %s GROUP BY year, month ORDER BY year DESC, month DESC LIMIT 1",
        (user_id,),
    )
    budget_row = cur.fetchone()
    current_budget = float(budget_row[2]) if budget_row else 0.0

    return {
        "category_count": category_count,
        "expense_count": expense_count,
        "total_spent": float(total_spent),
        "current_budget": current_budget,
    }
