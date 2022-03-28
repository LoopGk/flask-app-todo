print("Llamando al package")

from flask import Flask, render_template

app = Flask(__name__)

from todo import routes