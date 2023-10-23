"""Module for test"""
import unittest

from custom_list import CustomList


class Test(unittest.TestCase):
    """Test class for customlist testing"""

    def test_sum_list_to_customlist(self):
        """Test sum where left element is list and right is customlist"""
        self.assertEqual([1, 2, 3] + CustomList([1, 2, 3, 4]), CustomList([2, 4, 6, 4]))

    def test_sum_customlist_to_list(self):
        """Test sum where left element is customlist and right is list"""
        self.assertEqual(CustomList([-3, -5, -7, 10]) + [3, 5, 7], CustomList([0, 0, 0, 10]))

    def test_sub_list_to_customlist(self):
        """Test sub where left element is list and right is customlist"""
        self.assertEqual([1, 2, 3] - CustomList([1, 2, 3, 4]), CustomList([0, 0, 0, -4]))

    def test_sub_customlist_to_list(self):
        """Test sub where left element is customlist and right is list"""
        self.assertEqual(CustomList([100, 32, -7, 10]) - [100, 32, -7], CustomList([0, 0, 0, 10]))

    def test_eq_true(self):
        """Test eq by sum of element's customlist's"""
        self.assertTrue(CustomList([10, 1]) == CustomList([9, 1, 1]))

    def test_eq_false(self):
        """Test eq by sum of element's customlist's"""
        self.assertFalse(CustomList([9, 1]) == CustomList([9, 1, 1]))

    def test_ne_true(self):
        """Test ne eq by sum of element's customlist's"""
        self.assertTrue(CustomList([10, 1]) != CustomList([9, 1]))

    def test_ne_false(self):
        """Test ne eq by sum of element's customlist's"""
        self.assertFalse(CustomList([10, 1]) != CustomList([9, 1, 1]))

    def test_gt_true(self):
        """Test gt sum of element's customlist's"""
        self.assertTrue(CustomList([9]) > CustomList([3, 3, 2]))

    def test_gt_false(self):
        """Test gt by sum of element's customlist's"""
        self.assertFalse(CustomList([9]) > CustomList([3, 3, 3]))

    def test_ge_true(self):
        """Test ge by sum of element's customlist's"""
        self.assertTrue(CustomList([9]) >= CustomList([3, 3, 3]))

    def test_ge_false(self):
        """Test ge by sum of element's customlist's"""
        self.assertFalse(CustomList([9]) >= CustomList([3, 3, 4]))


if __name__ == "__main__":
    unittest.main()
