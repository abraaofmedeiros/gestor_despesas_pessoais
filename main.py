from App import app
from Logged import *
from NotLogged import *

print("Bem Vindo ao gestor de despesas pessoais!")

def display_menu():
    """Função que apresenta o menu de opções. Ela irá verificar se tem um usuário logado, e apresentar o menu de opções adequado"""
    if app.get_active_user() == None:
        display_logged_out_menu()
    else:
        display_logged_in_menu()

# A aplicação irá sempre estar executando a função de mostrar o menu.
while True:
    display_menu()
