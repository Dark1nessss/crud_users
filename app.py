from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/managment_crud_users"
mongo = PyMongo(app)

# Todos os dados utilizadores
utilizadores_mongodb = mongo.db.utilizadores.find()

# Se meter aqui o users
# jinja2.exceptions.UndefinedError: 'dict object' has no attribute 'id'
#users = list(utilizadores_mongodb)


# Primeiro tentar buscar os users a partir do mongodb
@app.route("/")
def index():
    # Mas aqui nao mostra os users, mesmo existindo dados na tabela
    users = list(utilizadores_mongodb)
    for i in users:
        print(i)
    return render_template("index.html", users=users, str=str)

# Aqui funciona se adicionar um user, mas no index, nao mostra os users
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        mongo.db.utilizadores.insert_one({"username": username, "email": email})
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if request.method == "POST":
        user["name"] = request.form["name"]
        user["email"] = request.form["email"]
        return redirect(url_for("index"))
    return render_template("edit_user.html", user=user)

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return redirect(url_for("index"))

# Rotas API users
@app.route("/api/users", methods=["GET"])
def api_users():
    utilizadores_mongodb = mongo.db.utilizadores.find()
    utilizadores = list(utilizadores_mongodb)
    for i in utilizadores:
        print(i)
    return render_template("utilizadores.html", utilizadores=utilizadores)

if __name__ == "__main__":
    app.run(debug=True)