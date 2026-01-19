from abc import ABC, abstractmethod

class NotificationService(ABC):

    @abstractmethod
    def send_notification(self,message):
        pass

class EmailNotificationService(NotificationService):

    def send_notification(self, message):
        print(f"sending notificaiton through email ::{message}")
        