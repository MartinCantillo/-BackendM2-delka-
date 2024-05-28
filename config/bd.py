from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

user = "CodeDelka"
password = "Adel12345"
direc = "CodeDelka.mysql.pythonanywhere-services.com"
namebd = "CodeDelka$bdMovil2"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "movil2"

db = SQLAlchemy(app)
ma = Marshmallow(app)
