from App import app
from models.usuario import *

def display_logged_out_menu():
    """Apresenta o menu para o usuário não logado, recebe uma opção do usuário e executa a respectiva função"""

    # Apresenta Menu
    print("Menu - Selecione uma das opções abaixo:")
    print("1 - Login")
    print("2 - Registar")
    
    # Recebe opção do usuário 
    option = input("Digite o número da opção desejada: ")

    # Verifica opção do usuário e encaminha para a função correspondente
    match option:
        case "1":
            login()
        case "2":
            register()
    
def register():
    print("Registar Novo Usuário")

    # Recebe nome
    name = input("Como deseja ser chamado?")

    if name == "0":
        return
        
    # Recebe username
    while True:
        username = input("Digite um nome de usuário: (0 para sair) ")

        if username == "0":
            return

        if checar_username(username):
            print("Usuário já existe, tente outro.")
        else:
            break

    # Recebe senha
    while True:
        password = input("Digite uma senha: ")
        password_confirmation = input("Confirme a senha: ")

        if password != password_confirmation or len(password) < 8:
            print("Senhas não conferem, tente novamente.")
        else:
            break

    # Recebe meta mensal
    while True:
        meta_mensal = float(input("Qual é a sua meta de gastos mensal? (Digite apenas números)"))
        if(meta_mensal <= 0):
            print("Meta inválida, tente novamente.")
        else:
            break

    # Armazena usuário no Banco de Dados
    inserir_usuario(name, username, password, meta_mensal)
    print("Usuário cadastrado com sucesso!")

def login():
    print("Login")

    # Recebe nome de usuário
    while True:
        username = input("Digite seu nome de usuário: (0 para sair) ")

        # Cancela o login caso o usuário tenha digitado zero
        if username == "0":
            return
        
        user = get_usuario(username)

        # Usuário encontrado, seguir para a próxima etapa
        if user is not None:
            break

    # Recebe a senha
    password = input("Digite sua senha: ")

    # Verifica a senha
    if user["senha"] == password:
        app.set_active_user(user)
        print("Login efetuado com sucesso!")
        return
        
    print("Usuário ou senha inválidos, tente novamente.")
 
