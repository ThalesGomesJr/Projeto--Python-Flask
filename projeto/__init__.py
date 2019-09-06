from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SECRET_KEY'] = 'secret'

#login_manager = LoginManager(app)
db = SQLAlchemy(app)

lm = LoginManager(app)