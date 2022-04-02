print("Llamando al package")

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Instance modules
db = SQLAlchemy(app)

from todo import routes
from todo import models