'''
Patrón DataMapper: nuestras entidades no conocen nada relativo a 
cómo éstas son persistidas en la base de datos.
'''

class User:

    def __init__(self, name, email, password):
        self.name     = name
        self.email    = email
        self.password = password

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password