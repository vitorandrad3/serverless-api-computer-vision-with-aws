from src.aws.rekognition.functions.detect_faces import get_faces_and_emotions
from src.aws.s3.functions.get_date import get_date
from src.utils.get_user_input import get_input
import json


def v2_vision(event, context):

    try:
        bucket, image_name = get_input(event)

        url = f"https://s3.amazonaws.com/{bucket}/{image_name}"

        image_data = get_faces_and_emotions(bucket, image_name)

        date = get_date(bucket, image_name)

        response_data = {
            "url_to_image": url,
            "created_image": date,
            "faces": image_data
        }

        api_return = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response_data)
        }

        return api_return

    except Exception as err:
        api_return = {"statusCode": err.status_code,
                      "headers": {
                          "Content-Type": "application/json"
                      },
                      "body": json.dumps({"error": err.message})}

        return api_return
