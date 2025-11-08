from sqlalchemy.orm import Session
from app.db.models import Feedback, Analysis

class FeedbackRepo:
    def __init__(self, db: Session): self.db = db
    def create(self, content: str) -> Feedback:
        f = Feedback(content=content)
        self.db.add(f); self.db.commit(); self.db.refresh(f)
        return f
    def get(self, id: int) -> Feedback | None:
        return self.db.get(Feedback, id)
    def mark_processed(self, id: int):
        f = self.get(id)
        if f:
            f.processed = True
            self.db.commit()

class AnalysisRepo:
    def __init__(self, db: Session): self.db = db
    def create(self, **kwargs) -> Analysis:
        a = Analysis(**kwargs)
        self.db.add(a); self.db.commit(); self.db.refresh(a)
        return a