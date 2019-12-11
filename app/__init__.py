from flask import Flask
app = Flask(__name__)

from config import Config
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy(app)
migrate=Migrate(app, db)

from flask_login import LoginManager
login=LoginManager(app)
login.login_view='login'

from app import routes, models