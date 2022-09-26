#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def normal_list(self):
        self.assertEqual(max_integer([1, 3, 7, 11]), 11)

    def test_2(self):
        self.assertEqual(max_integer([1, 11, 7]), 11)

    def test_3(self):
        self.assertEqual(max_integer([11, 1, 7]), 11)

    def empty_list(self):
        self.assertRaises(TypeError, max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
