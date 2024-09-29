from fastapi import FastAPI
from api import router as api_router
from views.employees.api import router as employees

app = FastAPI(title="Практическое задание")
app.include_router(api_router)
app.include_router(employees)