from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class Register(BaseModel):
    email: EmailStr
    password: str


class Login(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr


class CategoryCreate(BaseModel):
    name: str = Field(..., example="Groceries")


class Category(BaseModel):
    id: int
    name: str


class ExpenseCreate(BaseModel):
    category_id: Optional[int] = Field(None, example=1)
    amount: float = Field(..., gt=0, example=49.99)
    description: Optional[str] = Field(None, example="Monthly coffee and snacks")
    spent_at: Optional[datetime] = Field(None, example="2026-06-16T14:30:00Z")


class Expense(BaseModel):
    id: int
    category_id: Optional[int]
    amount: float
    description: Optional[str]
    spent_at: datetime
    created_at: datetime


class BudgetCreate(BaseModel):
    category_id: Optional[int] = Field(None, example=1)
    monthly_limit: float = Field(..., gt=0, example=1500.0)
    month: int = Field(..., ge=1, le=12, example=6)
    year: int = Field(..., ge=2000, example=2026)


class Budget(BaseModel):
    id: int
    category_id: Optional[int]
    monthly_limit: float
    month: int
    year: int
    created_at: datetime


class Report(BaseModel):
    category: str
    total_spent: float


class DashboardResponse(BaseModel):
    category_count: int
    expense_count: int
    total_spent: float
    current_budget: float
