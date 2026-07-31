#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Test with a descending list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_no_argument(self):
        """Test with no argument"""
        self.assertEqual(max_integer(), None)

    def test_one_element(self):
        """Test with a list of one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, -2, 3]), 5)

    def test_same_elements(self):
        """Test with a list where all elements are the same"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        """Test with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)


if __name__ == "__main__":
    unittest.main()
