from Utils import S3ClientAdapter,AzureBlobClientAdapter
from SDKs import S3Client, AzureBlobClient


if __name__ == '__main__':
    s3_client = S3Client("us-east-1")
    azure_client = AzureBlobClient()
    
    s3_adapter = S3ClientAdapter(s3_client)
    azure_adapter = AzureBlobClientAdapter(azure_client)

    s3_adapter.upload_file("bucket1","file1.txt","data1")
    azure_adapter.upload_file("azure_store","file2.txt","data2")





