import boto3
from dotenv import load_dotenv
from os import getenv as env

load_dotenv()

boto_session = boto3.Session(aws_access_key_id=env('aws_access_key_id'),
                             aws_secret_access_key=env('aws_secret_access_key'),
                             region_name=env('region_name'))