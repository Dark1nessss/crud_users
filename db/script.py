import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Setup da base de dados
def setupDB(db_name):
    # Criar a base de dados
    db = client[db_name]

    # Verifica se já existe a base de dados
    if db_name not in client.list_database_names():
        print(f"Base de dados '{db_name}' criada com sucesso!")
    
    # Criar coleção utilizadores
    utilizadores = db["utilizadores"]
    if "utilizadores" not in db.list_collection_names():
        print(f"Coleção utilizadores criada com sucesso!")
    return db, utilizadores

def inserirUtilizador(
        username,
        primeiro_nome,
        ultimo_nome,
        email,
        morada,
        telefone,
        descricao
):
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    user01 = {
        "username": username,
        "primeiro_nome": primeiro_nome,
        "ultimo_nome": ultimo_nome,
        "email": email,
        "morada": morada,
        "telefone": telefone,
        "descricao": descricao
    }
    documento_inserido_user01 = colecao_utilizadores.insert_one(user01)
    if documento_inserido_user01:
        print(f"Utilizador '{username}' inserido com sucesso!")

def pesquisarPrimeiroDocumento():
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    primeiro_user = colecao_utilizadores.find_one()
    print(primeiro_user)

def pesquisarUserUsername(Username):
    base_de_dados, colecao_utilizadores = setupDB("managment_crud_users")
    documento_query = colecao_utilizadores.find({"username": Username})
    for res in documento_query:
        print(res)

setupDB("managment_crud_users")
inserirUtilizador("tskxz", "tanjil", "khan", "tanjil@gmail.com", "Rua de Sobreira 505", 123412341, "utilizador comum")
pesquisarPrimeiroDocumento()