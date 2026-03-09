import typing
import datetime
from .NotificationType import NotificationType


if typing.TYPE_CHECKING:
    from Models import User



class Notification:

    def __init__(self, sender: 'User', receiver: 'User', content: str, type: 'NotificationType'):
        self.__sender = sender
        self.__receiver = receiver
        self.__content = content
        self.__timestamp = datetime.datetime.now()
        self.__type = type

    # --- Sender ---
    def get_sender(self) -> 'User':
        return self.__sender

    def set_sender(self, sender: 'User') -> None:
        self.__sender = sender

    # --- Receiver ---
    def get_receiver(self) -> 'User':
        return self.__receiver

    def set_receiver(self, receiver: 'User') -> None:
        self.__receiver = receiver

    # --- Content ---
    def get_content(self) -> str:
        return self.__content

    def set_content(self, content: str) -> None:
        self.__content = content

    # --- Timestamp ---
    def get_timestamp(self) -> datetime.datetime:
        return self.__timestamp

    def set_timestamp(self, timestamp: datetime.datetime) -> None:
        self.__timestamp = timestamp

    # --- Type ---
    def get_type(self) -> 'NotificationType':
        return self.__type

    def set_type(self, type: 'NotificationType') -> None:
        self.__type = type

    def __str__(self):
        return f"[{self.__type.name}] From {self.__sender.get_username()} → {self.__receiver.get_username()}: {self.__content} ({self.__timestamp})"
