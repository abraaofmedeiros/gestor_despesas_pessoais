from database.init_db import get_db

class App:
    def __init__(self):
        self.expenses = []
        self.active_user = None
        self.db = get_db()

    def get_active_user(self):
        return self.active_user
    
    def set_active_user(self, active_user):
        self.active_user = active_user

    def check_username_existance(self, username):
        return any(user["username"] == username for user in self.users)
    
    def add_user(self, user):
        self.users.append(user)
    

app = App()