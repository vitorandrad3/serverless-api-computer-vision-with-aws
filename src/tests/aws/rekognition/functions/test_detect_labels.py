from src.aws.rekognition.functions.detect_labels import detect_labels
from src.aws.rekognition.rekognition_client import rekognition
from src.tests.mocks.constants_mocks import *
from src.models.error_model import APIError
from unittest import TestCase
import unittest.mock as mock


class TestDetectLabels(TestCase):

    @mock.patch.object(rekognition, "detect_labels")
    def test_detect_labels_success(self, mock_detect_labels):
        mock_detect_labels.return_value = {
            'Labels': [{
                'Confidence': 'test_confidence',
                'Name': 'test_name'

            }]
        }

        response = detect_labels(bucket, image_name)

        self.assertEqual(
            response, [{'Confidence': 'test_confidence', 'Name': 'test_name'}])

    @mock.patch.object(rekognition, "detect_labels")
    def test_detect_labels_error_invalid_s3_object(self, mock_detect_labels):
        mock_detect_labels.side_effect = rekognition.exceptions.InvalidS3ObjectException(
            error_response=error_response, operation_name='detect_labels')

        with self.assertRaises(APIError) as cm:
            detect_labels(bucket, image_name)

        err = cm.exception

        self.assertEqual(err.status_code, 404)
        self.assertEqual(err.message, 'Image not found!')

    @mock.patch.object(rekognition, "detect_labels")
    def test_detect_labels_error_access_denied(self, mock_detect_labels):
        mock_detect_labels.side_effect = rekognition.exceptions.AccessDeniedException(
            error_response=error_response, operation_name='detect_labels')

        with self.assertRaises(APIError) as cm:
            detect_labels(bucket, image_name)

        err = cm.exception
        self.assertEqual(
            err.status_code, 401)
        self.assertEqual(
            err.message, "Invalid Credentials")

    @mock.patch.object(rekognition, "detect_labels")
    def test_detect_labels_error_invalid_parameter(self, mock_detect_labels):
        mock_detect_labels.side_effect = rekognition.exceptions.InvalidParameterException(
            error_response=error_response, operation_name='detect_labels')

        with self.assertRaises(APIError) as cm:
            detect_labels(bucket, image_name)

        err = cm.exception
        self.assertEqual(
            err.status_code, 406)
        self.assertEqual(
            err.message, 'Invalid parameter (bucket or image name) type')

    @mock.patch.object(rekognition, "detect_labels")
    def test_detect_labels_error_invalid_image_format(self, mock_detect_labels):
        mock_detect_labels.side_effect = rekognition.exceptions.InvalidImageFormatException(
            error_response=error_response, operation_name='detect_labels')

        with self.assertRaises(APIError) as cm:
            detect_labels(bucket, image_name)

        err = cm.exception

        self.assertEqual(
            err.status_code, 406)
        self.assertEqual(
            err.message, 'Invalid image format')

    @mock.patch.object(rekognition, "detect_labels")
    def test_detect_labels_error_unexpected(self, mock_detect_labels):
        mock_detect_labels.side_effect = TypeError()

        with self.assertRaises(APIError) as cm:
            detect_labels(bucket, image_name)

        err = cm.exception

        self.assertEqual(
            err.status_code, 500)
        self.assertEqual(
            err.message, 'unexpected error: ')
