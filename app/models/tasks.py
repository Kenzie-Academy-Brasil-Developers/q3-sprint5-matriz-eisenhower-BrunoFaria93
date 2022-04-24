from email.policy import default
from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship

print(f"{__name__} DB -> {id(db)}")

@dataclass
class Tasks(db.Model):

    tasks_id: int
    name: str
    description: str
    duration: int
    importance: int
    urgency: int


    __tablename__ = "tasks"

    tasks_id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)

    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.eisenhower_id"), nullable=False)

    eisenhower = relationship("Eisenhowers", back_populates="tasks")