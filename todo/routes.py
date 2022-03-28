from flask import render_template
from todo import app

# Rutas
@app.route("/")
def index():
    return render_template("hola.html", title = "Home")