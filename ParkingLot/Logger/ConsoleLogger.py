from .Logger import Logger


class ConsoleLogger(Logger):

    instance = None

    @staticmethod
    def get_instance():
        if ConsoleLogger.instance is None:
            ConsoleLogger.instance = ConsoleLogger()
        return ConsoleLogger.instance

    def log(self,message):
        print(message)
