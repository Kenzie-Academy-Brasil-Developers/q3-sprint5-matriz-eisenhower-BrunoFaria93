from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Singleton
db = SQLAlchemy()

print(f"{__name__} DB -> {id(db)}")


def init_app(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.db = db

    from app import models

