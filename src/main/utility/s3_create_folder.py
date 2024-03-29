from src.main.utility.s3_client_object import S3ClientProvider
from resources.dev import config
from src.main.utility.encrypt_decrypt import *

# get S3 client object

s3 = S3ClientProvider(decrypt(config.aws_access_key), decrypt(config.aws_secret_key)).get_client()

# get the list of folder in S3 bucket

response = s3.list_objects_v2(Bucket=config.bucket_name)
s3_bucket_object_list = [obj['Key'] for obj in response['Contents']]

# list of directories to be created in s3 bucket

s3_directories = [config.s3_customer_datamart_directory
    , config.s3_error_directory
    , config.s3_source_directory
    , config.s3_processed_directory
    , config.s3_sales_datamart_directory]

# if directory name not in list of contents in S3 bucket then create

for obj in s3_directories:
    if obj not in s3_bucket_object_list:
        s3.put_object(Bucket=config.bucket_name, Key=obj)
