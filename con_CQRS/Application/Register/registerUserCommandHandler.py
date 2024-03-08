from Application.Register.userCreator import UserCreator

from Application.nameValue     import NameValue
from Application.emailValue    import EmailValue
from Application.passwordValue import PasswordValue

class RegisterUserCommandHandler:

    def __init__(self, user_repository):
        
        self.user_creator = UserCreator(user_repository)

    def handle(self, command):

        # convertimos los primitivos del command en VO
        name = NameValue(command.name)
        email = EmailValue(command.email)
        password = PasswordValue(command.password)

        self.user_creator.create_user(name.value(), email.value(), password.value())
        