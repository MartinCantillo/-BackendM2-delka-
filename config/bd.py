from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/bdtest'
user = "CodeDelka"
password = "Adel12345"
direc = "CodeDelka.mysql.pythonanywhere-services.com"
namebd = "CodeDelka$bdMovil2"
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{direc}/{namebd}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "movil2"

bd = SQLAlchemy(app)
ma = Marshmallow(app)
