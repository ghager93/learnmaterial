from app import db


class GifsModel(db.Model):
    __tablename__ = 'gifs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    description = db.Column(db.String(200))
    path = db.Column(db.String(64))
    link = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())
    tags = db.Column(db.String(200))
    use_link = db.Column(db.Boolean)

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
            'tags': self.tags,
            'use_link': 'True' if self.use_link else 'False'
        }
