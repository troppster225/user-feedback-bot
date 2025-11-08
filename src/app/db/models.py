from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from datetime import datetime
from app.db.base import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    analysis = relationship("Analysis", back_populates="feedback", uselist=False)

class Analysis(Base):
    __tablename__ = "analysis"
    id: Mapped[int] = mapped_column(primary_key=True)
    feedback_id: Mapped[int] = mapped_column(ForeignKey("feedback.id"))
    sentiment: Mapped[str | None]
    topic: Mapped[str | None]
    summary: Mapped[str | None]
    model_version: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    feedback = relationship("Feedback", back_populates="analysis")