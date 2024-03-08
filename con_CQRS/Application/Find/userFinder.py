# caso de uso: buscar un usuario por su email

class UserFinder():

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def search_user_by_email(self, email):
        self.user_repository.search_user_by_email(email)
        


