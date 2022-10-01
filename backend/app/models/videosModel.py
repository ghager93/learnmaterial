from app import db


class VideosModel(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    description = db.Column(db.String(200))
<<<<<<< HEAD
    url = db.Column(db.String(64))
    youtube_id = db.Column(db.String(64))
=======
    link = db.Column(db.String(64))
>>>>>>> 665bdec34af27d620c77e8d5df317e8bd38b5ad5
    timestamp = db.Column(db.DateTime())
    tags = db.Column(db.String(200))
    length = db.Column(db.Integer)
    thumbnail_link = db.Column(db.String(64))
<<<<<<< HEAD
    user = db.Column(db.Integer, db.ForeignKey("users.id"))

    def to_dict(self):
        return {
=======

    def to_dict(self):
        return {
            'id': self.id,
>>>>>>> 665bdec34af27d620c77e8d5df317e8bd38b5ad5
            'name': self.name,
            'title': self.title,
            'author': self.author,
            'description': self.description,
<<<<<<< HEAD
            'url': self.url,
            'timestamp': self.timestamp,
            'tags': self.tags,
            'length': self.length,
            'thumbnail_link': self.thumbnail_link,
            'user': self.user
=======
            'link': self.link,
            'timestamp': self.timestamp,
            'tags': self.tags,
            'length': self.length,
            'thumbnail_link': self.thumbnail_link
>>>>>>> 665bdec34af27d620c77e8d5df317e8bd38b5ad5
        }
