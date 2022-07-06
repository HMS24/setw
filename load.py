import boto3
from settings import get_settings

setting = get_settings()

access_key = setting['AWS_ACCESS_KEY']
secret_key = setting['AWS_SECRET_KEY']
bucket_name = setting['AWS_S3_BUCKET_NAME']


def upload_file(filepath):
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    s3_filename = f'original_{path.basename(filepath)}'
    s3.upload_file(filepath, bucket_name, s3_filename)
