from Utils import IFileRepository, FileRepository, FileCompressor, FileEncrypter

if __name__ == '__main__':
    
    file_handler: IFileRepository = FileRepository()

    #writing data as it is into file.
    #file_handler.write_file("sample.txt", "Hello World")

    #in case of encyrption is required.
    file_handler = FileEncrypter(file_handler)
    #file_handler.write_file("sample.txt", "Hello World")

    #in case of both encryption and compression is required.
    file_handler = FileCompressor(file_handler)
    file_handler.write_file("sample.txt", "Hello World")


