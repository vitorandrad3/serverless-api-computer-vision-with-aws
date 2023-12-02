from src.utils.get_user_input import get_input
from unittest import TestCase
import unittest.mock as mock
from src.models.error_model import APIError
import json


class TestGetUserInput(TestCase):

    def test_valid_user_post(self):
        user_post = {
            "body": json.dumps({
                "bucket": "sprint8",
                "imageName": "bird.jpg"
            })
        }

        bucket, image_name = get_input(user_post)

        self.assertEqual(bucket, 'sprint8')
        self.assertEqual(image_name, 'bird.jpg')
    
    
    @mock.patch.object(json, "loads")
    def test_invalid_user_post(self, mock_json_loads):
        user_post = {
            "body": json.dumps({
                "bucket": "sprint8",
                "imageName": "bird.jpg"
            })
        }
        
        mock_json_loads.side_effect = TypeError()

        
        with self.assertRaises(APIError):
            get_input(user_post)
    


