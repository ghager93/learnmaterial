from app import db


class VideosModel(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    description = db.Column(db.Text)
    url = db.Column(db.String(64))
    youtube_id = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())
    tags = db.Column(db.String(200))
    length = db.Column(db.Integer)
    thumbnail_link = db.Column(db.String(64))
    user = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_dict(self):
        return {
            'name': self.name,
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'url': self.url,
            'youtube_id': self.youtube_id,
            'timestamp': self.timestamp,
            'tags': self.tags,
            'length': self.length,
            'thumbnail_link': self.thumbnail_link,
            'user': self.user,
        }
