from .FileRepository import IFileRepository

class FileEncrypter(IFileRepository): #Providing encryption flexibility to the data before writing into file.


    def __init__(self, wrapee: IFileRepository):
        self.repo: IFileRepository = wrapee

    def _encrypt_AES(self, data):
        data = "# " + data + " #"
        return data
    
    def _decrypt_AES(self, data):
        data = data[1:-1]
        return data

    def write_file(self, file_name, data):
        data = self._encrypt_AES(data)
        print(f"[FileEncrypter] Encrypted data {data}")
        self.repo.write_file(file_name, data)


    def read_file(self, file_name):
        data = self.repo.read_file(file_name)
        data = self._decrypt_AES(data)
        return f"{file_name} file_contents {data}"