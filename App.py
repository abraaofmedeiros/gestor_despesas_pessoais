# Importa a função get_db para acessar o banco de dados
from database.init_db import get_db

class App:
    def __init__(self):
         # Inicializa atributos da classe: lista de despesas e usuário ativo
        self.expenses = []
        self.active_user = None
        self.db = get_db() # Obtém acesso ao banco de dados

    def get_active_user(self):
        # Retorna o usuário atualmente ativo no sistema
        return self.active_user
    
    def set_active_user(self, active_user):
        # Define um usuário como o ativo no sistema
        self.active_user = active_user

    def check_username_existance(self, username):
        # Verifica se o nome de usuário já existe na lista de usuários
        return any(user["username"] == username for user in self.users)
    
    def add_user(self, user):
         # Adiciona um novo usuário à lista de usuários
        self.users.append(user)
    

app = App()
