from dataclasses import field
from datetime import datetime

from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db


class TokenBlockList:
    __tablename__ = "token_block_list"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    jti: str = field(default=None, metadata={"sa": db.Column(db.String(36), nullable=False, index=True)})
    created_at: datetime = field(default=None, metadata={"sa": db.Column(db.DateTime, nullable=False)})

    Schema = Schema
