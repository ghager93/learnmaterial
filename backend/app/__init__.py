from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

from flask_admin.contrib.sqla import ModelView

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)

login_manager = LoginManager(app)

admin = Admin(app, name="learn-material", template_mode="bootstrap3")

from app.views import (
    testView, 
    articlesView, 
    codeSnippetsView,
    gifsView,
    projectIdeasView,
    usersView,
    videosView,
    accountsView
)
app.register_blueprint(testView.mod, url_prefix='/test')
app.register_blueprint(articlesView.mod, url_prefix='/api/articles')
app.register_blueprint(codeSnippetsView.mod, url_prefix='/api/codesnippets')
app.register_blueprint(gifsView.mod, url_prefix='/api/gifs')
app.register_blueprint(projectIdeasView.mod, url_prefix='/api/projectIdeas')
app.register_blueprint(videosView.mod, url_prefix='/api/videos')
app.register_blueprint(usersView.mod, url_prefix='/api/users')
app.register_blueprint(accountsView.mod, url_prefix='/api/accounts')

from app.models import usersModel

admin.add_view(ModelView(usersModel.UsersModel, db.session))


if __name__ != "__main__":
    ...

if __name__ == "__main__":
    app.run()
