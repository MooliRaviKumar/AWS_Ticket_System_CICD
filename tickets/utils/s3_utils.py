import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os


AWS_REGION = 'ap-south-1'
AWS_S3_BUCKET_NAME = 's3uploadingfilebucket'

s3_client = boto3.client(
    's3',
    region_name=AWS_REGION
)

def upload_to_s3(file_obj, file_name, folder="attachments"):
    """Uploads a file to S3 and returns the public URL"""
    try:
        s3_path = f"{folder}/{file_name}"
        s3_client.upload_fileobj(
            file_obj,
            AWS_S3_BUCKET_NAME,
            s3_path
        )

        url = f"https://{AWS_S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{s3_path}"
        return url

    except NoCredentialsError:
        print(" AWS credentials not found.")
        return None
    except ClientError as e:
        print(f"Upload error: {e}")
        return None
