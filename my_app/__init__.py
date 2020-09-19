import os
from flask import Flask, session, request
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager

app = Flask(__name__)

#load main config
app.config.from_pyfile('../config.py') 

import my_app.views
