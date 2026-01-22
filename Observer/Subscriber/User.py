from abc import ABC, abstractmethod



class User(ABC):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return "User: {0}".format(self.name)
    
    @abstractmethod
    def notify(self,message):
        pass