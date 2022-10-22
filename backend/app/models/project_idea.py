from dataclasses import field
from datetime import datetime

from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db


@db.Model.registry.mapped
@dataclass
class ProjectIdea:
    __tablename__ = "project_ideas"
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    name: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    description: str = field(default=None, metadata={"sa": db.Column(db.String(200))})
    body: str = field(default=None, metadata={"sa": db.Column(db.Text())})
    created_at: datetime = field(default=None, metadata={"sa": db.Column(db.DateTime())})
    tags: str = field(default=None, metadata={"sa": db.Column(db.String(200))})

    Schema = Schema
