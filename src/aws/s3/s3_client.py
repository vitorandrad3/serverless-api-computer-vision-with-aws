from src.aws.boto_session import boto_session

s3 = boto_session.client(service_name='s3')