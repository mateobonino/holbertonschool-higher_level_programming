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

    def test_4(self):
        self.assertEqual(max_integer([12, -10, 6]), 12)

    def test_5(self):
        self.assertEqual(max_integer([1]), 1)

    def test_6(self):
        self.assertEqual(max_integer([-5, -10, -3, -2]), -2)

    def test_6(self):
        self.assertEqual(max_integer([100, 500, 700]), 700)

    def test_7(self):
        self.assertEqual(max_integer([]), None)

    def empty_list(self):
        self.assertRaises(TypeError, max_integer, None)

    


if __name__ == "__main__":
    unittest.main()
