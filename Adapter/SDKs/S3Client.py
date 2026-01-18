
class S3Client(): #usually this class will be available through 3rd partly SDKs.So creating basic methods

    def __init__(self, region):
        self.region = region
    
    def put_object(self,bucket_name, key, data):
        #uploading logic of file in aws s3.
        print(f"uploading {key} file into s3bucket{bucket_name}.")
        

