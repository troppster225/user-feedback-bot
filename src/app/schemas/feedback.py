from pydantic import BaseModel
from datetime import datetime

class FeedbackCreate(BaseModel):
    content: str

class FeedbackRead(BaseModel):
    id: int
    content: str
    created_at: datetime
    model_config = {"from_attributes": True}