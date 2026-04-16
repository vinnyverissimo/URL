import boto3
from app.core.config import settings

def create_table():
    # Conecta ao DynamoDB Local do Docker
    dynamodb = boto3.resource(
        'dynamodb', 
        endpoint_url=settings.DYNAMODB_URL,
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
    )
    
    try:
        table = dynamodb.create_table(
            TableName='ShortenedURLs',
            KeySchema=[
                {'AttributeName': 'short_key', 'KeyType': 'HASH'}  # Partition Key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'short_key', 'AttributeType': 'S'}
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        print(f"Tabela {table.table_name} criada com sucesso!")
    except Exception as e:
        print(f"Erro ou tabela já existente: {e}")

if __name__ == "__main__":
    create_table()