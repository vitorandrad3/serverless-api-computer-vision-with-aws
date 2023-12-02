from src.aws.s3.functions.get_date import get_date
from src.models.error_model import APIError
from src.tests.mocks.constants_mocks import *
from src.aws.s3.s3_client import s3
from unittest import TestCase
import unittest.mock as mock


class TestGetDate(TestCase):

    @mock.patch.object(s3, "get_object")
    def test_get_date(self, mock_get_object):
        mock_get_object.return_value = {
            'LastModified': '2023-10-23 15:18:48+00:00'
        }

        bucket_name = 'test_bucket'
        image_name = 'image_name'

        response = get_date(bucket_name, image_name)

        self.assertEqual(response, '23-10-2023 12:18:48')

    @mock.patch.object(s3, "get_object")
    def test_get_date_error_no_such_key(self, mock_get_date_error_no_such_key):
        mock_get_date_error_no_such_key.side_effect = s3.exceptions.NoSuchKey(
            error_response=error_response, operation_name='get_object')

        bucket = 'test_bucket'
        image_name = 'image_name'

        with self.assertRaises(APIError) as cm:
            get_date(bucket, image_name)

        err = cm.exception
        self.assertEqual(
            err.status_code, 404)
        self.assertEqual(
            err.message, 'Object not found')

    @mock.patch.object(s3, "get_object")
    def test_get_date_error_invalid_object_state(self, mock_get_date_error_invalid_object_state):
        mock_get_date_error_invalid_object_state.side_effect = s3.exceptions.InvalidObjectState(
            error_response=error_response, operation_name='get_object')

        bucket = 'test_bucket'
        image_name = 'image_name'

        with self.assertRaises(APIError) as cm:
            get_date(bucket, image_name)

        err = cm.exception

        self.assertEqual(
            err.status_code, 410)
        self.assertEqual(
            err.message, 'Object not available')

    @mock.patch.object(s3, "get_object")
    def test_get_date_error_unexpected(self, mock_get_date_error_unexpected):
        mock_get_date_error_unexpected.side_effect = Exception()

        bucket = 'test_bucket'
        image_name = 'image_name'

        with self.assertRaises(APIError) as cm:
            get_date(bucket, image_name)

        err = cm.exception

        self.assertEqual(
            err.status_code, 500)
        self.assertEqual(
            err.message, 'unexpected error: ')
