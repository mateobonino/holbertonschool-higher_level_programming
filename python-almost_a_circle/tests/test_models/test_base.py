#!/usr/bin/python3


import unittest
from models.base import Base

class Test_Base(unittest.TestCase):
    def check_1(self):
        base1 = Base()
        self.assertEqual(base1.id, 1)
