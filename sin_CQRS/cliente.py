from user import User
from userManager import UserManager

user  = User('Maria','maria@gmail.com','3243445')
user1 = User('Pedro','pedro@gmail.com','3243445')
user2 = User('Juan' ,'juan@gmail.com' ,'3243445')
user3 = User('Marta','marta@gmail.com','3243445')

userManager = UserManager()
userManager.register_user(user)
userManager.register_user(user1)
userManager.register_user(user2)
userManager.register_user(user3)

userFound = userManager.search_user_by_email('maria@gmail.com')