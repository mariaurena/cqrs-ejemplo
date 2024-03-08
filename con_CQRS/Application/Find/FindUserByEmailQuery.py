# query porque solo lee el estado actual del sistema
# DTO

class FindUserByEmailQuery():

    def __init__(self, email):
        self.email = email