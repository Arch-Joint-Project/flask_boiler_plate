from enum import unique
import uuid
from dataclasses import dataclass
from app import db
from sqlalchemy.dialects.postgresql import UUID

@dataclass
class User(db.Model):
    id: str
    email: str
    username: str
    password: str


    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)



