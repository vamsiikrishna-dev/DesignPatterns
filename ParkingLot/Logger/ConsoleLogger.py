from .Logger import Logger
import threading

class ConsoleLogger(Logger):

    instance = None
    _lock = threading.Lock()

    def __init__(self):
        if ConsoleLogger.instance is not None:
            raise Exception("ConsoleLogger is a singleton")

    @staticmethod
    def get_instance():
        if ConsoleLogger.instance is None:
            with ConsoleLogger._lock:
                if ConsoleLogger.instance is None:
                    ConsoleLogger.instance = ConsoleLogger()
        return ConsoleLogger.instance

    def log(self,message):
        print(message)
