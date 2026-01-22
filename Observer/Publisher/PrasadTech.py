from .Channel import Channel

class PrasadTech(Channel):

    def __init__(self):
        super().__init__()
        self.videos = []

    def upload(self, video):
        print(f"Uploading Video to the channel :{video}")
        self.notify(str(video))

        