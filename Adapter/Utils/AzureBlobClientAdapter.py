from SDKs import AzureBlobClient
from .FileUploader import FileUploader

class AzureBlobClientAdapter(FileUploader):

    def __init__(self, client: AzureBlobClient):
        self.azure_client = client

    def upload_file(self, bucket_id, file_name, data):
        self.azure_client.upload_blob(bucket_id, file_name, data)

