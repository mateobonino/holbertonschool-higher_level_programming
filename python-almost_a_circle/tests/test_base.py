#!/usr/bin/python3


import unittest
from models.base import Base


class Test_Base(unittest.TestCase):
    def test_1(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)

        base2 = Base()
        self.assertEqual(base2.id, 2)

        base3 = Base(89)
        self.assertEqual(base3.id, 89)

if __name__ == "__main__":
    unittest.main()
