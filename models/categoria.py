from App import app

db = app.db

def inserir_categoria(nome, user):
    """
    Insere uma nova categoria na tabela 'categoria'.
    """
    cursor = db.cursor()
    cursor.execute("INSERT INTO categoria (nome_categoria, usuario) VALUES (?, ?)", (nome, user))
    db.commit()

def get_user_categories(user_id):
    """
    Retorna todas as categorias da tabela 'categoria' para o usuário com id 'user_id'.
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM categoria WHERE usuario = ?", (user_id,))
    return [dict(linha) for linha in cursor.fetchall()]
