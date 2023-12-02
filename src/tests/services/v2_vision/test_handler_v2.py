from src.services.v2_vision.handler import v2_vision
from unittest import TestCase
import unittest.mock as mock
from src.models.error_model import APIError
import json

bucket = 'sprint8'
image_name = 'bird.jpg'
mock_image_data = [
    {
        "position": {
            "Height": 'test',
            "Left": 'test',
            "Top": 'test',
            "Width": 'test'
        },
        "classified_emotion": 'test',
        "classified_emotion_confidence": 'test'
    }
]


class TestV1Vision(TestCase):

    @mock.patch('src.services.v2_vision.handler.get_faces_and_emotions', return_value=mock_image_data)
    def test_success_v2_vision(self, mock_obj):

        response = v2_vision(
            {'body': json.dumps({'bucket': bucket, 'imageName': image_name})}, None)

        response_data = {
            "url_to_image": f"https://s3.amazonaws.com/{bucket}/{image_name}",
            "created_image": "23-10-2023 12:18:48",
            "faces": mock_image_data
        }

        api_return = {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps(response_data)
        }

        self.assertEqual(
            response, api_return)

    @mock.patch('src.services.v2_vision.handler.get_faces_and_emotions', side_effect=APIError(status_code=400, message='test'))
    def test_exception_v2_vision(self, mock_obj):

        response = v2_vision(
            {'body': json.dumps({'bucket': bucket, 'imageName': image_name})}, None)

        api_return = {"statusCode": 400,
                      "headers": {
                          "Content-Type": "application/json"
                      },
                      "body": json.dumps({"error": 'test'})}

        self.assertEqual(
            response, api_return)
