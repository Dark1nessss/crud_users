from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from db.script import inserirUtilizador, pesquisarTodosUtilizadores, pesquisarUserPorID, atualizarUtilizador, deletarUtilizador

app = Flask(__name__)

documents = [
    {"Movie Title": "Inception", "Director": "Christopher Nolan", "Genre": ["Action", "Sci-Fi", "Thriller"], "score": 8.8},
    {"Movie Title": "The Dark Knight", "Director": "Christopher Nolan", "Genre": ["Action", "Crime", "Drama"], "score": 9.0},
    {"Movie Title": "Interstellar", "Director": "Christopher Nolan", "Genre": ["Adventure", "Drama", "Sci-Fi"], "score": 8.6},
    {"Movie Title": "The Matrix", "Director": "Lana Wachowski, Lilly Wachowski", "Genre": ["Action", "Sci-Fi"], "score": 8.7},
    {"Movie Title": "Pulp Fiction", "Director": "Quentin Tarantino", "Genre": ["Crime", "Drama"], "score": 8.9},
    {"Movie Title": "Fight Club", "Director": "David Fincher", "Genre": ["Drama"], "score": 8.8},
    {"Movie Title": "Forrest Gump", "Director": "Robert Zemeckis", "Genre": ["Drama", "Romance"], "score": 8.8},
    {"Movie Title": "The Shawshank Redemption", "Director": "Frank Darabont", "Genre": ["Drama"], "score": 9.3},
    {"Movie Title": "The Godfather", "Director": "Francis Ford Coppola", "Genre": ["Crime", "Drama"], "score": 9.2},
    {"Movie Title": "The Godfather: Part II", "Director": "Francis Ford Coppola", "Genre": ["Crime", "Drama"], "score": 9.0}
]

def setup_db(db_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]

    collection = db["imdb"]
    existing_movies = list(collection.find({}))
    if not existing_movies:
        collection.insert_many(documents)
        print("Initial movies inserted into MongoDB.")

    return db, collection

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
    db, collection = setup_db("films")
    app.run(debug=True)
