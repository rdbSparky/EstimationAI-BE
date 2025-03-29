import boto3
import uuid
from botocore.config import Config
from django.conf import settings

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION,
    config=Config(s3={"addressing_style": "path"}, signature_version="s3v4"),
)


def generate_file_key(file_name):
    """
    Generate a unique file key for S3 storage using UUID.
    Format: <UUID>.<file_extension>
    """
    file_extension = file_name.split(".")[-1] if "." in file_name else "bin"
    unique_file_name = f"{uuid.uuid4()}.{file_extension}"
    return unique_file_name  # No AWS_MEDIA_PATH dependency


class S3Object:
    """Handles file upload to S3"""

    def __init__(self, file, file_name):
        self.file = file
        self.file_name = file_name

    def upload(self):
        """Upload file to S3 and return media key"""
        file_key = generate_file_key(self.file_name)

        s3.upload_fileobj(
            self.file,
            settings.AWS_BUCKET,
            file_key,
            ExtraArgs={"ACL": "public-read"},
        )

        return file_key

def generate_signed_url(media_key, expiration=3600):
    """
    Generate a pre-signed URL for accessing a file in S3.

    Args:
        media_key (str): The S3 object key (file path).
        expiration (int): Time in seconds until the URL expires (default: 1 hour).

    Returns:
        str: Signed URL if successful, else None.
    """
    try:
        signed_url = s3.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": settings.AWS_BUCKET,
                "Key": media_key,
            },
            ExpiresIn=expiration,
        )
        return signed_url
    except Exception as e:
        print(f"Error generating signed URL: {e}")
        return None
