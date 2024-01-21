from resources.dev import config
from src.main.utility.encrypt_decrypt import *
from src.main.utility.s3_client_object import S3ClientProvider
from src.main.utility.logging_config import *


aws_access_key = config.aws_access_key

aws_secret_key = config.aws_secret_key

s3_client_provider = S3ClientProvider(decrypt(aws_access_key), decrypt(aws_secret_key))

s3_client = s3_client_provider.get_client()

response = s3_client.list_buckets()

print([bucket['Name'] for bucket in response['Buckets']])
logger.info("List of buckets: %s", response['Buckets'])

