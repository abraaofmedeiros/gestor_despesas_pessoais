from App import app
db = app.db

def inserir_despesa(usuario, categoria, nome_despesa, valor, data):
    """
    Insere uma nova despesa na tabela 'despesa'.
    """
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO despesa (usuario, categoria, nome_despesa, valor, data) VALUES (?, ?, ?, ?, ?)",
        (usuario, categoria, nome_despesa, valor, data)
    )
    db.commit()

def get_user_expenses(user_id):
    """
    Retorna todas as despesas da tabela 'despesa'.
    """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM despesa WHERE usuario = ? ORDER BY data DESC", (user_id,))
    return [dict(linha) for linha in cursor.fetchall()]
