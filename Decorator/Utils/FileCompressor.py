from .FileRepository import IFileRepository

class FileCompressor(IFileRepository): #Compressing data before writing into file.


    def __init__(self, wrapee: IFileRepository):
        self.repo: IFileRepository = wrapee

    def _compress_base64(self, data):
        return f"$${data}$$"
    
    def _parse_base64(self, data):  
        return data[2:-2]

    def write_file(self, file_name, data):
        data1 = data
        data = self._compress_base64(data)
        print(f"[FileCompressor] {data1} compressed to {data}")
        self.repo.write_file(file_name, data)

    def read_file(self, file_name):
        data = self.repo.read_file(file_name)
        data = self._parse_base64(data)
        return f"data parsing is done. data::{data}"