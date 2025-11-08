from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.feedback import FeedbackCreate, FeedbackRead
from app.db.repositories import FeedbackRepo

router = APIRouter(prefix="/feedback", tags=["feedback"])

@router.post("/", response_model=FeedbackRead, status_code=201)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    repo = FeedbackRepo(db)
    fb = repo.create(content=feedback.content)
    return fb

@router.get("/{id}", response_model=FeedbackRead)
def read_feedback(id: int, db: Session = Depends(get_db)):
    repo = FeedbackRepo(db)
    fb = repo.get(id)
    if not fb:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return fb