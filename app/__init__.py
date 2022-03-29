import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from os import path
# from flask_login import LoginManager, login_manager

db = SQLAlchemy()
DB_NAME = "mywebappdatabase.db"



app = Flask(__name__)
app.config["SECRET_KEY"] = "JHHGUIF HUHUH HHUF UH"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(DB_NAME)
db.init_app(app)

from . import views

from .models import Patients_details
#  create_database(app)


#  login_manager = LoginManager()
#  login_manager.login_view = "admin.login"
#  login_manager.init_app(app)

#  @login_manager.user_loader
#  def load_user(id):
#      return User.query.get(int(id))

 

#  return app


def create_database(app):
    # if not path.exists("app/" + DB_NAME):
    if not os.path.exists(f"C:/Users/NEU/Documents/Flask Tuts/app/{DB_NAME}"):
        db.create_all(app=app)
        print("Database created!!")


create_database(app)
