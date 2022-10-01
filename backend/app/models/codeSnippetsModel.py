from app import db


class CodeSnippetsModel(db.Model):
    __tablename__ = 'codeSnippets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    description = db.Column(db.String(200))
    body = db.Column(db.Text())
    link = db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())
    language = db.Column(db.String(64))
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
            'language': self.language,
            'tags': self.tags
        }