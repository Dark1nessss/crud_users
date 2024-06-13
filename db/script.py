import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")

def setupDB(db_name):
    db = client[db_name]

    if db_name not in client.list_database_names():
        print(f"Database '{db_name}' created successfully!")
    
    movies = db["imdb"]
    if "imdb" not in db.list_collection_names():
        print(f"Collection 'imdb' created successfully!")
    return db, movies

def inserirFilme(title, director, genre, score):
    base_de_dados, colecao_filmes = setupDB("films")
    movie = {
        "Movie Title": title,
        "Director": director,
        "Genre": genre,
        "score": score
    }
    documento_inserido = colecao_filmes.insert_one(movie)
    if documento_inserido:
        print(f"Movie '{title}' inserted successfully!")

def pesquisarTodosFilmes():
    base_de_dados, colecao_filmes = setupDB("films")
    return list(colecao_filmes.find())

def pesquisarFilmePorID(film_id):
    base_de_dados, colecao_filmes = setupDB("films")
    return colecao_filmes.find_one({"_id": ObjectId(film_id)})

def atualizarFilme(film_id, title, director, genre, score):
    base_de_dados, colecao_filmes = setupDB("films")
    colecao_filmes.update_one(
        {"_id": ObjectId(film_id)}, 
        {"$set": {"Movie Title": title, "Director": director, "Genre": genre, "score": score}}
    )
    print(f"Movie with ID {film_id} updated!")

def deletarFilme(film_id):
    base_de_dados, colecao_filmes = setupDB("films")
    colecao_filmes.delete_one({"_id": ObjectId(film_id)})
    print(f"Movie with ID {film_id} deleted!")

def limpar():
    base_de_dados, colecao_filmes = setupDB("films")
    colecao_filmes.drop()

if __name__ == "__main__":
    setupDB("films")
    
    inserirFilme("Inception", "Christopher Nolan", ["Action", "Sci-Fi", "Thriller"], 8.8)
    inserirFilme("The Dark Knight", "Christopher Nolan", ["Action", "Crime", "Drama"], 9.0)
    inserirFilme("Interstellar", "Christopher Nolan", ["Adventure", "Drama", "Sci-Fi"], 8.6)

    print("All movies:")
    for movie in pesquisarTodosFilmes():
        print(movie)

    film_id = pesquisarTodosFilmes()[0]["_id"]
    print(f"\nMovie with ID {film_id}:")
    print(pesquisarFilmePorID(film_id))

    atualizarFilme(film_id, "Inception", "Christopher Nolan", ["Action", "Sci-Fi", "Thriller"], 8.9)

    deletarFilme(film_id)
