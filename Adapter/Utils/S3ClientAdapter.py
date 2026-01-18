from SDKs import S3Client
from .FileUploader import FileUploader

class S3ClientAdapter(FileUploader):

    def __init__(self, client: S3Client):
        self.s3_client = client

    def upload_file(self, bucket_id, file_name, data):
        self.s3_client.put_object(bucket_id, file_name, data)
