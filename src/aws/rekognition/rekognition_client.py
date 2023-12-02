from src.aws.boto_session import boto_session

rekognition = boto_session.client(service_name='rekognition')