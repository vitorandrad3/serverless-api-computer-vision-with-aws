from src.services.v1_vision.handler import v1_vision
from unittest import TestCase
import unittest.mock as mock
from src.models.error_model import APIError
import json


bucket = 'sprint8'
image_name = 'bird.jpg'
mock_labels = [
    {
        "Confidence": 99.99836730957031,
        "Name": "Animal"
    },]


class TestV1Vision(TestCase):

    @mock.patch('src.services.v1_vision.handler.detect_labels', return_value=mock_labels)
    def test_success_v1_vision(self, mock_obj):

        response = v1_vision(
            {'body': json.dumps({'bucket': bucket, 'imageName': image_name})}, None)

        response_data = {
            "url_to_image": f"https://s3.amazonaws.com/{bucket}/{image_name}",
            "created_image": "23-10-2023 12:18:48",
            "labels": mock_labels
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

    @mock.patch('src.services.v1_vision.handler.detect_labels', side_effect=APIError(status_code=400, message='test'))
    def test_exception_v1_vision(self, mock_obj):

        response = v1_vision(
            {'body': json.dumps({'bucket': bucket, 'imageName': image_name})}, None)

        api_return = {"statusCode": 400,
                      "headers": {
                          "Content-Type": "application/json"
                      },
                      "body": json.dumps({"error": 'test'})}

        self.assertEqual(
            response, api_return)
