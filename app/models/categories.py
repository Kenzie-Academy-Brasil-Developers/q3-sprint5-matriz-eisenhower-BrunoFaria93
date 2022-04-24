from email.policy import default
from app.configs.database import db
from sqlalchemy import Column, Integer, String, Text
from dataclasses import dataclass
from sqlalchemy.orm import relationship

print(f"{__name__} DB -> {id(db)}")

@dataclass
class Categories(db.Model):
    category_id: int
    name: str
    description: str


    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

