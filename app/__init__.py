import os
from flask import Flask
# from flask import Flask, request, flash, jsonify, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

lm = LoginManager()
lm.init_app(app)

app.jinja_env.auto_reload = True

# models
from app.models import tables, forms
# controllers
from app.controllers import default