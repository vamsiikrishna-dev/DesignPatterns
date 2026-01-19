from abc import ABC, abstractmethod

class IFileRepository(ABC):

    @abstractmethod
    def write_file(self, file_name, data):
        pass

    @abstractmethod
    def read_file(self, file_name):
        pass