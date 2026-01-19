from .IFileRepository import IFileRepository

class FileRepository(IFileRepository): #This is the actual file writer.
    def write_file(self, file_name, data):
        print(f"[FileRepository] written into file {file_name} with data {data}")

    def read_file(self, file_name): #Need to add logic to read from a file. For now returning a fixed string.
        return f"Hello World"



