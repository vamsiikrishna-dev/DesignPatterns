from Publisher import Channel, BarbelReview, PrasadTech
from Subscriber import User, YoutubeUser

if __name__ == "__main__":

    prasad_channel = PrasadTech()
    subscriber1 = YoutubeUser("Vamsi")
    subscriber2 = YoutubeUser("Krishna")
    prasad_channel.add_subsriber(subscriber1)
    prasad_channel.add_subsriber(subscriber2)
    prasad_channel.upload("Best mobiles under 10000")
    prasad_channel.remove_subscriber(subscriber2)
    prasad_channel.upload("Best laptop deals amazon big billion days")
