# command porque modifica el estado del sistema
# DTO

class RegisterUserCommand():

    def __init__(self, name, email, password):
        self.name     = name
        self.email    = email
        self.password = password
