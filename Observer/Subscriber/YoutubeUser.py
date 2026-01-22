from .User import User

class YoutubeUser(User):

    def __init__(self,name):
        super().__init__(name)

    def notify(self,message):
        print(f"{self} notified with {message}")