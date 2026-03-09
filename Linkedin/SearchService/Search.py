from abc import ABC, abstractmethod
from Models import User


class Search(ABC):


    @abstractmethod
    def search(self, keyword, users: list[User]):
        pass