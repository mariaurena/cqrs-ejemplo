# value object
class PasswordValue():

    def __init__(self, password):
        if not any(char.isupper() for char in password):
            raise ValueError("El password debe contener al menos una letra mayúscula")
        self.password = password

    def value(self):
        return self.password