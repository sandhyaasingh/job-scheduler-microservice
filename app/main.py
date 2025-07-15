from fastapi import FastAPI
from app.routers import jobs
from app.database import create_db

app = FastAPI(
    title="Job Scheduler Microservice",
    description="Schedule and manage jobs with customizable intervals.",
    version="1.0.0"
)

# Register API routes
app.include_router(jobs.router)

# Startup event: Create DB tables
@app.on_event("startup")
def startup_event():
    create_db()
    print("Job Scheduler Service is up!")
