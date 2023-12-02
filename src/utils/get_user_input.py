import json
from src.models.error_model import APIError


def get_input(event):
    try:

        body = json.loads(event["body"])
        bucket = body["bucket"]
        image_name = body["imageName"]
       
        return bucket, image_name

    except Exception as err:
        raise APIError(status_code=500,
                       message=f'Invalid body post: {str(err)}')
