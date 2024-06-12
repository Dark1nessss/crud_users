from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from db.script import inserirUtilizador, pesquisarTodosUtilizadores, pesquisarUserPorID, atualizarUtilizador, deletarUtilizador

app = Flask(__name__)

@app.route("/")
def index():
    users = pesquisarTodosUtilizadores()
    return render_template("index.html", users=users, str=str)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        inserirUtilizador(username, email)
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<string:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = pesquisarUserPorID(ObjectId(user_id))
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        atualizarUtilizador(ObjectId(user_id), username, email)
        return redirect(url_for("index"))
    return render_template("edit_user.html", user=user, str=str)

@app.route("/delete_user/<string:user_id>")
def delete_user(user_id):
    deletarUtilizador(ObjectId(user_id))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
