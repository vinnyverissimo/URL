import boto3
from app.core.config import settings

_dynamodb = None

def get_dynamodb():
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource(
            'dynamodb',
            endpoint_url=settings.DYNAMODB_URL,
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
    return _dynamodb

def get_table():
    db = get_dynamodb()
    return db.Table('ShortenedURLs')