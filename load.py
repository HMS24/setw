from os import path
from configparser import ConfigParser

import boto3

parser = ConfigParser()
parser.read('setup.conf')

access_key = parser.get('aws_boto_credentials', 'access_key')
secret_key = parser.get('aws_boto_credentials', 'secret_key')
bucket_name = parser.get('aws_boto_credentials', 'bucket_name')


def upload_file(filepath):
    s3 = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    s3_filename = f'original_{path.basename(filepath)}'
    s3.upload_file(filepath, bucket_name, s3_filename)
