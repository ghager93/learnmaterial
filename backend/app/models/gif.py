from dataclasses import field
from datetime import datetime

from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db


@db.Model.registry.mapped
@dataclass
class Gif:
    __tablename__ = 'gifs'
    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    name: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    local_path: str = field(default=None, metadata={"sa": db.Column(db.String(64))})
    created_at: datetime = field(default=None, metadata={"sa": db.Column(db.DateTime())})
    tags: str = field(default=None, metadata={"sa": db.Column(db.String(200))})
    use_link: bool = field(default=False, metadata={"sa": db.Column(db.Boolean)})

    Schema = Schema
