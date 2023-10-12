"""Module for test"""
import unittest
import time
from unittest.mock import Mock
from first_exercise import parse_json, callback_handler
from second_exercize import mean


class TestParsing(unittest.TestCase):
    """Test class for parsing json (first exercise)"""

    def test_callback_handler(self):
        """Test callback function"""
        self.assertEqual(callback_handler('Hello'), 'Found Hello')

    def test_occurrence(self):
        """Test there are such words in the keys for parsing"""
        self.assertTrue(
            len(
                parse_json(
                    json_str='{"person_id": 8220108, "name": "Michael Fitzgerald", "description": '
                             '"new second television sound news red ball investment '
                             '  thing throughout answer."}',
                    required_fields=['description'],
                    keywords=['the', 'I', 'new'],
                    keyword_callback=callback_handler
                )
            ) == 1
        )

    def test_empty(self):
        """Test there are NOT such words in the keys for parsing"""
        self.assertTrue(
            len(
                parse_json(
                    json_str='{"person_id": 8220108, "name": "Michael Fitzgerald", "description": '
                             '"second television sound news red ball investment '
                             'thing throughout answer."}',
                    required_fields=['description'],
                    keywords=['the', 'I', 'new'],
                    keyword_callback=callback_handler
                )
            ) == 0
        )


class TestMock(unittest.TestCase):
    """Test class calls count of mock object"""
    def setUp(self) -> None:
        self.keyword_callback = Mock()

    def test_count_mock(self):
        """Test for calculate calls of mock object"""
        for _ in range(10):
            self.keyword_callback()

        self.assertEqual(self.keyword_callback.call_count, 10)


class TestDecorator(unittest.TestCase):
    """Test class for decorator calculation least recent calls duration time"""

    def test_time(self):
        """Test for decorator calculation least recent calls duration time"""
        @mean(3)
        def sleeper(seconds):
            time.sleep(seconds)

        time_sleep = [0.1, 0.1, 0.1, 0.1, 0.2, 0.3]
        average_last_k_calls = 0
        for i in time_sleep:
            average_last_k_calls = sleeper(i)[1]

        self.assertEqual(round(average_last_k_calls, 1), 0.2)
