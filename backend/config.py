from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FLASK_ADMIN_SWATCH = "spacelab"

    SECRET_KEY = "deb78dcbe36faeafefb6534d56a38bdc0541e3591a6b59bab57636fc5043ac9c"

    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_COOKIE_SECURE = False
    JWT_SECRET_KEY = "deb78dcbe36faeafefb6534d56a38bdc0541e3591a6b59bab57636fc5043ac9c"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=10)
