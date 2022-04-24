from email.policy import default
from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship

print(f"{__name__} DB -> {id(db)}")

@dataclass
class TaskCategory(db.Model):
    id: int

    __tablename__ = "task_category"

    id = Column(Integer, primary_key=True)

    task_id = Column(Integer, ForeignKey("tasks.tasks_id"), nullable=False)
    
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
