from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
from sqlalchemy.orm import relationship

print(f"{__name__} DB -> {id(db)}")

@dataclass
class Eisenhowers(db.Model):

    eisenhower_id: int
    type: str

    __tablename__ = "eisenhowers"

    eisenhower_id = Column(Integer, primary_key=True)
    type = Column(String(100))

    tasks = relationship("Tasks", back_populates="eisenhower")