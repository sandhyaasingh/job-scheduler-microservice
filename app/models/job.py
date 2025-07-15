from sqlalchemy import Column, Integer, String, DateTime, Text
from app.database import Base
import datetime

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    schedule_type = Column(String, nullable=False)  # e.g., 'cron', 'interval'
    cron_expression = Column(String, nullable=True)  # e.g., '0 9 * * MON'
    last_run = Column(DateTime, default=None)
    next_run = Column(DateTime, default=None)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
