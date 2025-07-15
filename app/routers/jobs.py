from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.job import JobCreate, JobResponse
from app.models.job import Job
from app.database import get_db
from app.services.scheduler import schedule_job
from datetime import datetime
from typing import List

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.post("/", response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(
        name=job.name,
        description=job.description,
        schedule_type=job.schedule_type,
        cron_expression=job.cron_expression,
        last_run=None,
        next_run=None,
        created_at=datetime.utcnow()
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)

    # Schedule job immediately
    schedule_job(db_job)

    return db_job

@router.get("/", response_model=List[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    return db.query(Job).all()

@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
