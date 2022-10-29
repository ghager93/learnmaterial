from dataclasses import field
from datetime import datetime

from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db


@db.Model.registry.mapped
@dataclass
class Video:
    __tablename__ = "videos"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    name: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    title: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    author: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    description: str = field(default=None, metadata={"sa": db.Column(db.Text)})
    url: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    youtube_id: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    created_at: datetime = field(default=None, metadata={"sa": db.Column(db.DateTime())})
    tags: str = field(default=None, metadata={"sa": db.Column(db.Text)})
    thumbnail_link: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    length: int = field(default=0, metadata={"sa": db.Column(db.Integer)})
    user: int = field(default=None, metadata={"sa": db.Column(db.Integer, db.ForeignKey("users.id"))})

    Schema = Schema