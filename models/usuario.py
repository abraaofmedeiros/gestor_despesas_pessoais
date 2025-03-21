from App import app

def inserir_usuario(nome, username, senha, meta_mensal):
    """
    Insere uma novo usuario na tabela 'usuarios'.
    """
    cursor = app.db.cursor()
    cursor.execute("INSERT INTO usuario (nome, username, senha, meta_mensal) VALUES (?, ?, ?, ?)", (nome, username, senha, meta_mensal))
    app.db.commit()

def listar_usuarios():
    """
    Retorna todas os usuarios da tabela 'usuario'.
    """
    cursor = app.db.cursor()
    cursor.execute("SELECT * FROM usuario")
    return cursor.fetchall()

def checar_username(username):
    """
    Retorna True se o username ja existe na tabela 'usuario', False caso contrario.
    """
    cursor = app.db.cursor()
    cursor.execute("SELECT * FROM usuario WHERE username = ?", (username,))
    return cursor.fetchone() is not None

def get_usuario(username):
    """
    Retorna o usuario com o username passado.
    """
    cursor = app.db.cursor()
    cursor.execute("SELECT * FROM usuario WHERE username = ?", (username,))
    row = cursor.fetchone()

    return dict(row) if row else None

def get_usuario_by_id(user_id):
    """
    Retorna o usuario com o id passado.
    """
    cursor = app.db.cursor()
    cursor.execute("SELECT * FROM usuario WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    return dict(row) if row else None

def update_meta_mensal(user_id, nova_meta):
    """
    Atualiza apenas o campo 'meta_mensal' de um usuário.
    """
    cursor = app.db.cursor()
    cursor.execute("""
        UPDATE usuario
        SET meta_mensal = ?
        WHERE id = ?
    """, (nova_meta, user_id))
    app.db.commit()
