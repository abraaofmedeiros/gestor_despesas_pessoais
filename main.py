from App import app
from Logged import *
from NotLogged import *

print("Bem Vindo ao gestor de despesas pessoais!")

from models.usuario import get_usuario
app.set_active_user(get_usuario('admin'))

def display_menu():
    if app.get_active_user() == None:
        display_logged_out_menu()
    else:
        display_logged_in_menu()

while True:
    display_menu()