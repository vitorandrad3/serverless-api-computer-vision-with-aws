from src.aws.rekognition.functions.detect_faces import get_faces_and_emotions
from src.aws.rekognition.rekognition_client import rekognition
from unittest import TestCase
import unittest.mock as mock
from src.models.error_model import APIError
from src.tests.mocks.constants_mocks import *


class TestDetectFaces(TestCase):

    @mock.patch.object(rekognition, "detect_faces")
    def test_detect_faces_success_with_face(self, mock_detect_faces):
        mock_detect_faces.return_value = {
            'FaceDetails': [{
                'BoundingBox': 'test_position',
                'Emotions': [{'Type': 'test', 'Confidence': 'test_confidence'}],

            }]
        }

        response = get_faces_and_emotions(bucket, image_name)

        self.assertEqual(response, [{'positon': 'test_position', 'classified_emotion': 'test',
                         'classified_emotion_confidence': 'test_confidence'}])

    @mock.patch.object(rekognition, "detect_faces")
    def test_detect_faces_success_without_face(self, mock_detect_faces):
        mock_detect_faces.return_value = {
            'FaceDetails': None
        }

        response = get_faces_and_emotions(bucket, image_name)

        self.assertEqual(response, [{"position": {"Height": None, "Left": None, "Top": None,
                         "Width": None}, "classified_emotion": None, "classified_emotion_confidence": None}])

    @mock.patch.object(rekognition, "detect_faces")
    def test_detect_faces_error_Invalid_s3_object(self, mock_detect_faces):
        mock_detect_faces.side_effect = rekognition.exceptions.InvalidS3ObjectException(
            error_response=error_response, operation_name='detect_faces')

        with self.assertRaises(APIError) as cm:
            get_faces_and_emotions(bucket, image_name)

        err = cm.exception
        self.assertEqual(
            err.status_code, 404)
        self.assertEqual(
            err.message, 'Image not found!')

    @mock.patch.object(rekognition, "detect_faces")
    def test_detect_faces_error_invalid_parameter_exception(self, mock_detect_faces):

        mock_detect_faces.side_effect = rekognition.exceptions.InvalidParameterException(
            error_response=error_response, operation_name='detect_faces')

        with self.assertRaises(APIError) as cm:
            get_faces_and_emotions(bucket, image_name)

        err = cm.exception
        self.assertEqual(
            err.status_code, 404)
        self.assertEqual(
            err.message, 'Invalid parameter (bucket or image name) type')

    @mock.patch.object(rekognition, "detect_faces")
    def test_detect_faces_error_access_denied_exception(self, mock_detect_faces):
        mock_detect_faces.side_effect = rekognition.exceptions.AccessDeniedException(
            error_response=error_response, operation_name='detect_faces')

        with self.assertRaises(APIError) as cm:
            get_faces_and_emotions(bucket, image_name)

        err = cm.exception

        self.assertEqual(
            err.status_code, 401)
        self.assertEqual(
            err.message, 'Invalid Credentials')

    @mock.patch.object(rekognition, "detect_faces")
    def test_detect_faces_error_unexpected(self, mock_detect_faces):
        mock_detect_faces.side_effect = Exception()

        with self.assertRaises(APIError) as cm:
            get_faces_and_emotions(bucket, image_name)

        err = cm.exception

        self.assertEqual(
            err.status_code, 500)
        self.assertEqual(
            err.message, 'unexpected error: ')
