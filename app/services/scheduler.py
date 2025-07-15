from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.models.job import Job
from datetime import datetime
import time

# Background scheduler (runs in same app process)
scheduler = BackgroundScheduler()
scheduler.start()

# Dummy task for demonstration
def run_dummy_task(job_id: int, job_name: str):
    print(f"Running job {job_id}: {job_name} at {datetime.utcnow()}")

def schedule_job(job: Job):
    """
    Register a job with APScheduler using cron expression.
    """
    if job.schedule_type == "cron" and job.cron_expression:
        try:
            trigger = CronTrigger.from_crontab(job.cron_expression)

            scheduler.add_job(
                func=run_dummy_task,
                trigger=trigger,
                args=[job.id, job.name],
                id=str(job.id),
                replace_existing=True
            )

            print(f"Scheduled job {job.id}: {job.name} with cron '{job.cron_expression}'")

        except Exception as e:
            print(f"Failed to schedule job {job.id}: {e}")
