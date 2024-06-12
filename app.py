from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
# Temos de adicionar aqui a ligacao ao mongo...


# memoria local
users = []

@app.route("/")
def index():
    return render_template("index.html", users=users)

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        date = request.form["date"]
        users.append({"id": len(users) + 1, "name": name, "email": email, "date": date})
        return redirect(url_for("index"))
    return render_template("add_user.html")

@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if request.method == "POST":
        user["name"] = request.form["name"]
        user["email"] = request.form["email"]
        user["date"] = request.form["date"]
        return redirect(url_for("index"))
    return render_template("edit_user.html", user=user)

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    global users
    users = [user for user in users if user["id"] != user_id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)