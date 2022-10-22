from dataclasses import field
from datetime import datetime

from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db


@db.Model.registry.mapped
@dataclass
class Article:
    __tablename__ = "articles"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    name: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    title: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    author: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    description: str = field(default=None, metadata={"sa": db.Column(db.String(200))})
    body: str = field(default=None, metadata={"sa": db.Column(db.Text())})
    url: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    created_at: datetime = field(default=None, metadata={"sa": db.Column(db.DateTime())})
    tags: str = field(default=None, metadata={"sa": db.Column(db.String(200))})

    Schema = Schema
