from Infrastructure.userRepositoryMongoDB import UserRepositoryMongoDB

from Domain.CommandBus import CommandBus
from Domain.QueryBus   import QueryBus

from Application.Register.registerUserCommand import RegisterUserCommand
from Application.Register.registerUserCommandHandler import RegisterUserCommandHandler

from Application.Find.FindUserByEmailQuery import FindUserByEmailQuery
from Application.Find.FindUserByEmailQueryHandler import FindUserByEmailQueryHandler

# repositorio de usuarios: MongoDB
user_repository = UserRepositoryMongoDB()

command_bus = CommandBus()
query_bus   = QueryBus()

# registro de manejadores de los buses
register_user_command_handler = RegisterUserCommandHandler (user_repository)
find_user_command_handler     = FindUserByEmailQueryHandler(user_repository)

command_bus.register_handler(RegisterUserCommand, register_user_command_handler)
query_bus.register_handler  (FindUserByEmailQuery, find_user_command_handler)

# caso de uso: registrar a un usuario
register_user_command = RegisterUserCommand('Roberto', 'roberto@gmail.com', 'A234345453')
command_bus.handle(register_user_command)

# caso de uso: buscar un usuario por su correo
find_user_by_email_query = FindUserByEmailQuery('roberto@gmail.com')
query_bus.handle(find_user_by_email_query)

