from Application.emailValue import EmailValue
from Application.Find.userFinder import UserFinder

class FindUserByEmailQueryHandler:

    def __init__(self, user_repository):

        self.user_finder = UserFinder(user_repository)

    def handle(self, query):

        # convertimos los primitivos de la query en VO
        email = EmailValue(query.email)

        return self.user_finder.search_user_by_email(email.value())
