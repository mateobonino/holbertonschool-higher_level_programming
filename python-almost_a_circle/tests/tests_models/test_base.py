#!/usr/bin/python3


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Base().id, 1)

        self.assertEqual(Base().id, 2)

        self.assertEqual(Base(59).id, 59)

        self.assertEqual(Base().to_json_string([]), '[]')

if __name__ == "__main__":
    unittest.main()
