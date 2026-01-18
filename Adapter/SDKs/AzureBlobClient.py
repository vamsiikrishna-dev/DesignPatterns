
class AzureBlobClient(): #usually this class will be available through 3rd partly SDKs.So creating basic methods

    def upload_blob(self,container, key, data):
        #uploading logic of file in azure blob storage.
        print(f"uploading {key} into azureblob at {container}.")
        

