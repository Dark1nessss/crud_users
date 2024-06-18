from pymongo import MongoClient

def setup_db(db_name):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db["imdb"]
    return db, collection

def inserir_filme(title, director, genre, score):
    _, collection = setup_db("films")
    existing_movie = collection.find_one({"Movie Title": title})
    if existing_movie is None:
        movie = {
            "Movie Title": title,
            "Director": director,
            "Genre": genre,
            "score": score,
        }
        documento_inserido = collection.insert_one(movie)
        if documento_inserido:
            print(f"Movie '{title}' inserted successfully!")

def pesquisarTodosFilmes():
    _, collection = setup_db("films")
    return list(collection.find())

def pesquisarFilmePorID(film_id):
    _, collection = setup_db("films")
    return collection.find_one({"_id": film_id})

def atualizarFilme(film_id, title, director, genre, score):
    _, collection = setup_db("films")
    collection.update_one({"_id": film_id}, {"$set": {"Movie Title": title, "Director": director, "Genre": genre, "score": score}})
    print(f"Movie with ID {film_id} updated!")

def deletarFilme(film_id):
    _, collection = setup_db("films")
    collection.delete_one({"_id": film_id})
    print(f"Movie with ID {film_id} deleted!")