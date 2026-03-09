from .Notification import Notification

class NotificationService:

    def send_notification(self, notification: Notification):
        receiver = notification.get_receiver()
        receiver.get_inbox().append(notification)
        print(f"Notification sent to {receiver.get_username()}: {notification.get_content()}")

        
