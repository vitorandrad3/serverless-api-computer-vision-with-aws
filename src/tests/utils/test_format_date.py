from src.utils.format_date import format_date
from unittest import TestCase


class TestFormatDate(TestCase):

    def test_format_date1(self):
        formatted_date = format_date('2023-10-23 15:18:48+00:00')

        self.assertEqual(formatted_date, '23-10-2023 12:18:48')

    def test_format_date2(self):
        formatted_date = format_date('2022-05-20 15:18:48+00:00')

        self.assertEqual(formatted_date, '20-05-2022 12:18:48')
