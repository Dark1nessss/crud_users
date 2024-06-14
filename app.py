from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from db.script import inserir_filme, pesquisarTodosFilmes, pesquisarFilmePorID, atualizarFilme, deletarFilme

app = Flask(__name__)

# Insert initial movie data if not present
initial_movies = [
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

# Insert initial data if not already present
for movie in initial_movies:
    inserir_filme(movie["Movie Title"], movie["Director"], movie["Genre"], movie["score"])

@app.route("/")
def index():
    movies = pesquisarTodosFilmes()
    return render_template("index.html", movies=movies, str=str)

@app.route("/add_movie", methods=["GET", "POST"])
def add_movie():
    if request.method == "POST":
        title = request.form["title"]
        director = request.form["director"]
        genre = request.form.getlist("genre")
        score = float(request.form["score"])
        inserir_filme(title, director, genre, score)
        return redirect(url_for("index"))
    return render_template("add_movie.html")

@app.route("/edit_movie/<string:movie_id>", methods=["GET", "POST"])
def edit_movie(movie_id):
    movie = pesquisarFilmePorID(ObjectId(movie_id))
    if request.method == "POST":
        title = request.form["title"]
        director = request.form["director"]
        genre = request.form.getlist("genre")
        score = float(request.form["score"])
        atualizarFilme(ObjectId(movie_id), title, director, genre, score)
        return redirect(url_for("index"))
    return render_template("edit_movie.html", movie=movie, str=str)

@app.route("/delete_movie/<string:movie_id>")
def delete_movie(movie_id):
    deletarFilme(ObjectId(movie_id))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
