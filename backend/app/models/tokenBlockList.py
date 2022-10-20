from app import db


class TokenBlockList(db.Model):
    __tablename__ = "token_block_list"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
