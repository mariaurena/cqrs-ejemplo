# value object
class EmailValue():

    def __init__(self, email):
        if "@" not in email:
            raise ValueError("El email debe contener el símbolo '@'")
        self.email = email

    def value(self):
        return self.email