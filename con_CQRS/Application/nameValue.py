# value object
class NameValue():

    def __init__(self, name):
        if len(name) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")
        self.name = name

    def value(self):
        return self.name