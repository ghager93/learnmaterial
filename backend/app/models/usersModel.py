from flask_login import UserMixin
from app import db, login_manager, jwt_manager
from werkzeug.security import check_password_hash

class UsersModel(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    @jwt_manager.user_identity_loader
    def create_token(self):
        return {
            "username": self.username
        }

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email
        }
        

@login_manager.user_loader
def load_user(id):
    return db.session.query(UsersModel).get(int(id))
