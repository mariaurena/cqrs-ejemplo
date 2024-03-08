# caso de uso: registrar a un usuario

from Domain.user import User

class UserCreator():

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, name, email, password):
        user = User(name, email, password)
        self.user_repository.register_user(user)
        


