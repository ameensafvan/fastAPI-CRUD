from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import employee

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee CRUD API")


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": "Employee CRUD API is running. Go to /docs to test APIs."
    }
app.include_router(employee.router)
