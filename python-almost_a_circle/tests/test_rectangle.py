import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_2(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_3(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.id, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)