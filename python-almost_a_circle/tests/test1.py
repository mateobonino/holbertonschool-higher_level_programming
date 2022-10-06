#!/usr/bin/python3


import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    def test_2(self):
        a = Base()
        self.assertEqual(a.id, 1)
        b = Base(5)
        self.assertEqual(b.id, 5)