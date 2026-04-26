from contextlib import asynccontextmanager


from fastapi import FastAPI
from database import Database

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database connection
    print("Initializing database connection...")
    db = Database(
        host="localhost",
        dbname="your_db_name",
        user="your_db_user",
        password="your_db_password",
        port=5432
    )
    app.state.db = db
    yield
    print("Cleaning up resources...")
    # Cleanup code if needed (e.g., close database connections)

@app.get("/")
def read_root():
    return {"Hello": "World"}