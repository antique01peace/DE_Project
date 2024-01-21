from src.main.utility.s3_client_object import S3ClientProvider
from resources.dev import config
from src.main.utility.encrypt_decrypt import *

s3 = S3ClientProvider(decrypt(config.aws_access_key), decrypt(config.aws_secret_key)).get_client()

response = s3.list_objects_v2(Bucket=config.bucket_name)
s3_bucket_object_list = [obj['Key'] for obj in response['Contents']]

s3_directories = [config.s3_customer_datamart_directory
                , config.s3_error_directory
                , config.s3_source_directory
                , config.s3_processed_directory
                , config.s3_sales_datamart_directory]

for obj in s3_directories:
    if obj not in s3_bucket_object_list:
        s3.put_object(Bucket=config.bucket_name, Key=obj)




