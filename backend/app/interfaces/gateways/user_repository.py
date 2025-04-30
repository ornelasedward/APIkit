from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def insert(self, user):
        pass

    @abstractmethod
    def fetch_all(self):
        pass

    @abstractmethod
    def delete(self, user_id):
        pass
