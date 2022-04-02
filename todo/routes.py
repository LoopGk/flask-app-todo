from crypt import methods
import re
from flask import render_template, request, jsonify
from todo import app, db
from todo.models import User, Task

PATH_BASE_API = "/api/v1"

# Rutas
@app.route("/")
def index():
    return render_template("hola.html", title = "Home")

# API routes

@app.route(f'{PATH_BASE_API}/user/create', methods=['GET', 'POST'])
def create_user():
    if request.method == "POST":
        data = request.json
        username = data["username"]
        email = data["email"]
        password = data["password"]

        user = User(username = username, email = email, password = password)
        db.session.add(user)
        db.session.commit()
        msg = "Usuario creado"
    elif request.method == 'GET':
        msg = 'Este endpoint es para el registro de un nuevo usuario. Utilice el método POST'
    return {
        "code": 200,
        "msg": msg
    }

@app.route(f'{PATH_BASE_API}/users/all', methods=['GET'])
def get_users():
    response = []
    list_users = User.query.all()
    # "Serializar"
    for user in list_users:
        data = {"username":user.username, "email": user.email}
        response.append(data)
    return jsonify(response)

@app.route(f'{PATH_BASE_API}/task/create/<int:user_id>', methods=['GET', 'POST'])
def create_task(user_id):
    if request.method == 'POST':
        data = request.json
        title = data["title"]
        content = data["content"]
        is_done = data["isDone"]
        user_id = user_id

        task = Task(title = title, content = content, isDone = is_done, user_id = user_id)
        db.session.add(task)
        db.session.commit()
        msg = "Tarea creada exitosamente"
    elif request.method == 'GET':
        msg = 'Este endpoint es para la cración de una nueva tarea. Utilice el método POST'
    return {
        "code": 200,
        "msg": msg
    }

@app.route(f'{PATH_BASE_API}/task/getmytasks/<int:user_id>', methods=['GET'])
def get_my_tasks(user_id):
    response = []
    tasks = Task.query.filter_by(user_id = user_id)
    for task in tasks:
        data = {"id": task.id, "title": task.title, "content": task.content, "isDone": task.isDone, "date_posted": task.date_posted}
        response.append(data)
    return jsonify(response)