import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")


def setupDB(db_name):

    db = client[db_name]

    if db_name not in client.list_database_names():
        print(f"Base de dados '{db_name}' criada com sucesso!")
    
    utilizadores = db["utilizadores"]
    if "utilizadores" not in db.list_collection_names():
        print(f"Coleção utilizadores criada com sucesso!")
    return db, utilizadores

def inserirUtilizador(username, email):
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    user = {
        "username": username,
        "email": email
    }
    documento_inserido = colecao_utilizadores.insert_one(user)
    if documento_inserido:
        print(f"Utilizador '{username}' inserido com sucesso!")

def pesquisarTodosUtilizadores():
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    return list(colecao_utilizadores.find())

def pesquisarUserPorID(user_id):
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    return colecao_utilizadores.find_one({"_id": user_id})

def atualizarUtilizador(user_id, username, email):
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    colecao_utilizadores.update_one({"_id": user_id}, {"$set": {"username": username, "email": email}})
    print(f"Utilizador com ID {user_id} atualizado!")

def deletarUtilizador(user_id):
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    colecao_utilizadores.delete_one({"_id": user_id})
    print(f"Utilizador com ID {user_id} deletado!")


def limpar():
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    colecao_utilizadores.drop()

if __name__ == "__main__":
    setupDB("managment_crud_users")
    # Exemplo de inserção
    inserirUtilizador("user1", "user1@example.com")
    inserirUtilizador("user2", "user2@example.com")

    print("Todos os utilizadores:")
    for user in pesquisarTodosUtilizadores():
        print(user)

    user_id = pesquisarTodosUtilizadores()[0]["_id"]
    print(f"\nUtilizador com ID {user_id}:")
    print(pesquisarUserPorID(user_id))

    atualizarUtilizador(user_id, "user1_updated", "user1_updated@example.com")

    deletarUtilizador(user_id)