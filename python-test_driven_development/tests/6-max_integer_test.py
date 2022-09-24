#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def normal_list(self):
        self.assertEqual(max_integer([1, 3, 7, 11]), 11)

    def negative_expected(self):
        self.assertEqual(max_integer([-5, -15, -3, -6]), -15)

    def empty_list(self):
        self.assertEqual(max_integer([]), None)


if __name__ == "__main__":
    unittest.main()
