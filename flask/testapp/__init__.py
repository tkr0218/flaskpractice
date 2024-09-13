from flask import Flask

app = Flask(__name__)
app.config.from_object('testapp.config')
from flask_sqlalchemy import SQLAlchemy  # 追加

app = Flask(__name__)
app.config.from_object('testapp.config')

db = SQLAlchemy(app) 
from .models import employee 

import testapp.views