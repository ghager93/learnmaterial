from app import db

class TestModel(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    string1 = db.Column(db.String(64))
    num1 = db.Column(db.Integer)
    string2 = db.Column(db.String(64))

    def to_dict(self):
        return ({
            "id": self.id,
            "string1": self.string1,
            "num1": self.num1,
            "string2": self.string2
        })

    def __repr__(self):
        return f'<Test {self.id}>'