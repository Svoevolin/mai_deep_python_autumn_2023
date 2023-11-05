"""Module for test"""
import unittest
from lru_cache import LRUCache


class TestLRU(unittest.TestCase):
    """Test LRU"""

    def test_set_and_get_1(self):
        """Getting existing value"""
        lru = LRUCache(1)
        lru['1'] = 2
        self.assertEqual(lru['1'], 2)

    def test_set_and_get_2(self):
        """Getting an overridden key"""
        lru = LRUCache(1)
        lru['1'] = 2
        lru['1'] = 3
        self.assertEqual(lru['1'], 3)

    def test_set_and_get_3(self):
        """Test to remove an unused element after overriding another one"""
        lru = LRUCache(2)
        lru['1'] = 1
        lru['2'] = 2
        lru['1'] = 3
        lru['4'] = 4
        with self.assertRaises(KeyError):
            something = lru['2']

    def test_set_and_get_4(self):
        """Test for removing an unused element after getting another one"""
        lru = LRUCache(2)
        lru['1'] = 1
        lru['2'] = 2
        something = lru['1']
        lru['3'] = 3
        with self.assertRaises(KeyError):
            something = lru['2']
