from App import app
from models.usuario import *
    # Escolhe entre loga ou se registrar
def display_logged_out_menu():
    print("Menu - Selecione uma das opções abaixo:")
    print("1 - Login")
    print("2 - Registar")
    # digita 2 se precisar criar uma conta ou 1 se já tem uma conta 
    option = input("Digite o número da opção desejada: ")

    match option:
        case "1":
            login()
        case "2":
            register()
    # caso deseja criar uma nova conta
def register():
    print("Registar Novo Usuário")

    # Receber nome
    name = input("Como deseja ser chamado?")

    if name == "0":
        return
        
    # Receber username
    while True:
        username = input("Digite um nome de usuário: (0 para sair) ")

        if username == "0":
            return

        if checar_username(username):
            print("Usuário já existe, tente outro.")
        else:
            break

    # Receber senha
    while True:
        password = input("Digite uma senha: ")
        password_confirmation = input("Confirme a senha: ")

        if password != password_confirmation or len(password) < 8:
            print("Senhas não conferem, tente novamente.")
        else:
            break

    # Receber meta mensal
    while True:
        meta_mensal = float(input("Qual é a sua meta de gastos mensal? (Digite apenas números)"))
        if(meta_mensal <= 0):
            print("Meta inválida, tente novamente.")
        else:
            break

    # Armazenar usuário
    inserir_usuario(name, username, password, meta_mensal)
    print("Usuário cadastrado com sucesso!")
    # logar
def login():
    print("Login")
    
    while True:
        username = input("Digite seu nome de usuário: (0 para sair) ")
    # voutar
        if username == "0":
            return
        
        user = get_usuario(username)
        
        if user is not None:
            break

    password = input("Digite sua senha: ")

    if user["senha"] == password:
        app.set_active_user(user)
        print("Login efetuado com sucesso!")
        return
        
    print("Usuário ou senha inválidos, tente novamente.")
 
