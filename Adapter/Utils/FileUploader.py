from abc import ABC, abstractmethod

class FileUploader(ABC): #its the uploader service we provided to the clients.

    @abstractmethod
    def upload_file(self,file_name,data):
        pass
