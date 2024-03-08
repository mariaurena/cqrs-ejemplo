from abc import ABC, abstractmethod

class UserRepository(ABC):

    @abstractmethod
    def register_user(self, user):
        pass

    @abstractmethod
    def search_user_by_email(self, email):
        pass
