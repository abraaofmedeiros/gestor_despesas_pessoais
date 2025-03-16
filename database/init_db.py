import os
import sqlite3

DB_PATH = "database/app.db"

def create_database():
    """Inicializa o banco de dados com base no schema.sql."""
    with sqlite3.connect(DB_PATH) as conn:
        with open("database/schema.sql", "r") as f:
            conn.executescript(f.read())
        print("Banco de dados inicializado com sucesso!")

def conectar_banco():
    """Retorna uma conexão com o banco de dados."""
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row

    return db

def get_db():
    """Verifica se o banco de dados existe; caso contrário, cria."""
    if not os.path.exists(DB_PATH):
        print("Banco de dados não encontrado. Criando o banco de dados...")
        create_database()
    else:
        print("Banco de dados já existe. Conectando...")
    
    return conectar_banco()