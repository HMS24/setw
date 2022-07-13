import boto3
from setw.settings import get_settings

setting = get_settings()

access_key = setting['AWS_ACCESS_KEY']
secret_key = setting['AWS_SECRET_KEY']
bucket_name = setting['AWS_S3_BUCKET_NAME']


def upload_file_to_s3(filepath):
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    s3_filename = filepath
    s3.upload_file(filepath, bucket_name, s3_filename)
