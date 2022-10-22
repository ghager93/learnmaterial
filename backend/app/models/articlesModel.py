from dataclasses import field
from datetime import datetime

from marshmallow import Schema
from marshmallow_dataclass import dataclass

from app import db


@db.Model.registry.mapped
@dataclass
class Article:
    __tablename__ = "articles2"

    __sa_dataclass_metadata_key__ = "sa"

    id: int = field(init=False, metadata={"sa": db.Column(db.Integer, primary_key=True)})
    name: str = field(metadata={"sa": db.Column(db.String(64), unique=True)})
    title: str = field(metadata={"sa": db.Column(db.String(64))})
    # author: str = field(metadata={"sa": db.Column(db.String(64))})
    # description: str = field(metadata={"sa": db.Column(db.String(200))})
    # body: str = field(metadata={"sa": db.Column(db.Text())})
    # link: str = field(metadata={"sa": db.Column(db.String(64))})
    # timestamp: datetime = field(metadata={"sa": db.Column(db.DateTime())})
    # tags: str = field(metadata={"sa": db.Column(db.String(200))})

    Schema = Schema


class ArticlesModel(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    description = db.Column(db.String(200))
    body = db.Column(db.Text())
    link = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())
    tags = db.Column(db.String(200))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'body': self.body,
            'link': self.link,
            'timestamp': self.timestamp,
            'tags': self.tags
        }
