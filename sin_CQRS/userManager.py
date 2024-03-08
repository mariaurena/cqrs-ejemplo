from pymongo import MongoClient

class UserManager:

    def __init__(self):

        # Conectarse a la base de datos MongoDB
        self.client = MongoClient('localhost', 27017)

        # Seleccionar la base de datos
        self.db = self.client['users']

        # Seleccionar la colección
        self.collection = self.db['user']


    def register_user(self, user):

        new_user = {
            'name'    : user.get_name(),
            'email'   : user.get_email(),
            'password': user.get_password()
        }

        # evitar tener users repetidos con el mismo email
        user_in_bd = self.collection.find_one({'email': user.get_email()})

        if ( user_in_bd ):
            print(f"Ya existe un user con email { user.get_email() }")
            return None

        result = self.collection.insert_one(new_user)

        # verificar si la inserción fue exitosa
        if result.inserted_id:
            print("Nuevo user insertado con el ID:", result.inserted_id)
        else:
            print("Error al insertar al user")


    def search_user_by_email(self, email):

        user_found = None

        user_found = self.collection.find_one({'email': email})

        if user_found != None:
            print("Usuario encontrado con nombre:", user_found.get('name'))
        else:
            print("No se ha encontrado el usuario")

        return user_found