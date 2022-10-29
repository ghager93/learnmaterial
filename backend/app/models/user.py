from dataclasses import field
from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import check_password_hash
from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db, jwt_manager

@db.Model.registry.mapped
@dataclass
class User:
    __tablename__ = 'users'
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    password_hash: str = field(default=None, metadata={"sa": db.Column(db.String(128))})
    username: str = field(default=None, metadata={"sa": db.Column(db.String(64))})

    Schema = Schema

    @jwt_manager.user_identity_loader
    def create_token(self):
        return {
            "username": self.username
        }

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
