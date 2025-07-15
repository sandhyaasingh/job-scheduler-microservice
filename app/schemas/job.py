from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobCreate(BaseModel):
    name: str
    description: Optional[str] = None
    schedule_type: str  # 'cron'
    cron_expression: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    schedule_type: str
    cron_expression: Optional[str]
    last_run: Optional[datetime]
    next_run: Optional[datetime]
    created_at: datetime

    class Config:
        orm_mode = True
