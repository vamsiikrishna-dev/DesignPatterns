from Models import User, JobPosting, Profile
from NotificationService import NotificationService, Notification, NotificationType
from SearchService import SearchService

class Linkedin:

    def __init__(self):
        self.users = {}
        self.notify_service = NotificationService()
        self.search_service = SearchService()
        self.job_postings = []


    def register_user(self, user:User):
        self.users[user.get_username()] = user
    
    def login(self, username, password):
        user: User = self.users.get(username)
        if user and user.get_password() == password:
            print("Authentication Successful.")
            return user
        raise Exception("Login failed with invalid username and password")

    def send_connection_request(self, from_user, to_user:User):
        to_user.get_connection_requests().append(from_user)
    
    def accept_connection(self, user:User, target_user:User):
        user.get_connection_requests().remove(target_user)
        user.get_connections().append(target_user)
        target_user.get_connections().append(user)

    def post_job(self,job:JobPosting):
        self.job_postings.append(job)

    def create_profile(self, user:User, profile: Profile):
        user = self.users.get(user.get_username())
        user.set_profile(profile)
    
    def send_notification(self, sender: User, receiver: User, content: str, notification_type: NotificationType):
        notification = Notification(sender, receiver, content, notification_type)
        self.notify_service.send_notification(notification)
        return notification

    def search(self, keyword):
        return self.search_service.search(keyword, list(self.users.values()))


    

    




    