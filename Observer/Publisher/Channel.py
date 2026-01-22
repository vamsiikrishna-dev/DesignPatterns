from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Subscriber import User

class Channel(ABC):

    def __init__(self):
        self.subscribers = []

    def add_subsriber(self, subscriber: 'User'):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: 'User'):
        self.subscribers.remove(subscriber)

    @abstractmethod
    def upload(self,video):
        pass

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.notify(message)
    


