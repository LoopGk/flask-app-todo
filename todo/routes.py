from crypt import methods
from flask import render_template
from todo import app, db
from todo.models import Cliente

# Rutas
@app.route("/")
def index():
    return render_template("hola.html", title = "Home")

@app.route("/delete/", methods = ["POST"])
def delete():
    _id = 2
    Cliente.query.filter_by(id = _id).delete()
    db.session.commit()
    return {"msg": "Cliente eliminado"}