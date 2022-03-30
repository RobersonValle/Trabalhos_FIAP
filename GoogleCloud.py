# !pip install --upgrade google-cloud-storage
import os
from google.cloud import storage
import json

class GoogleCloud:
    
    
    def __init__(self,service_key_path=None):
        
        self._service_key_path= service_key_path
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_key_path
        self.storage_client= storage.Client()        
   
    # bucket_name = "data_lake_2022"
    # my_bucket = storage_client.get_bucket(bucket_name)
        
    def get_key (self):
        return self._service_key_path
            
        
    def upload_to_bucket(self,blob_name,file_path,bucket_name):
        try:
            bucket = self.storage_client.get_bucket(bucket_name)
            bucket.exists
            blob = bucket.blob(blob_name)
            blob.upload_from_filename (file_path)
            return True
        except Exception as e:
            print(e)
            return False

    def upload_blob_from_memory(self,bucket_name, contents, destination_blob_name):
        """Uploads a file to the bucket."""
        try:
        
            storage_client = storage.Client()
            bucket = self.storage_client.bucket(bucket_name)
            blob = bucket.blob(destination_blob_name)

            blob.upload_from_string(contents, content_type='application/json')
            return True
        except Exception as e:
            print(e)
            return False

    def download_blob_to_json_list(self,bucket_name, blob_name):
        try:
            bucket = self.storage_client.bucket(bucket_name)

            # blob = bucket.blob(blob_name)
            blob = bucket.get_blob(blob_name)
            contents = blob.download_as_bytes(raw_download=True)
            return json.loads(contents.decode('utf8') )

        except Exception as e:
                print(e)
                return False
    def get_list_blob(self,bucket_name, prefix):
            # bucket = self.storage_client.get_bucket(bucket_name)
            # print(list(bucket.list_blobs('blob')) )
            return list(self.storage_client.list_blobs(bucket_name,prefix=prefix))


if __name__ == "__main__":
    upload_blob_from_memory(
        bucket_name=sys.argv[1],
        contents=sys.argv[2],
        destination_blob_name=sys.argv[3],
    )