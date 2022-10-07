import unittest
from models.rectangle import Rectangle

class Test_Rectangle(unittest.TestCase):
    def test_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_2(self):
        rect2 = Rectangle(1, 2, 3)
        self.assertEqual(rect2.id, 10)
        self.assertEqual(rect2.width, 1)
        self.assertEqual(rect2.height, 2)
        self.assertEqual(rect2.x, 3)

    def test_3(self):
        rect3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect3.id, 11)
        self.assertEqual(rect3.width, 1)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 3)
        self.assertEqual(rect3.y, 4)

    def test_6(self):
        rect4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect4.id, 5)
        self.assertEqual(rect4.width, 1)
        self.assertEqual(rect4.height, 2)
        self.assertEqual(rect4.x, 3)
        self.assertEqual(rect4.y, 4)

    def test_7(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        
    def test_8(self):
        rect5 = Rectangle(3, 3)
        self.assertEqual(rect5.id, 12)
        self.assertEqual(rect5.width, 3)
        self.assertEqual(rect5.height, 3)
        self.assertEqual(rect5.area(), 9)

    def test_9(self):
        rect6 = Rectangle(3, 3, 3, 3)
        self.assertEqual(rect6.id, 13)
        self.assertEqual(rect6.width, 3)
        self.assertEqual(rect6.height, 3)
        self.assertEqual(rect6.area(), 9)
        self.assertEqual(rect6.__str__(), "[Rectangle] (13) 3/3 - 3/3")

    def test_10(self):
        rect7 = Rectangle(3, 2, 0, 0)
        self.assertEqual(rect7.display(), "###\n###\n")

    def test_11(self):
        rect8 = Rectangle(3, 2, 1, 2, 15)
        self.assertEqual(rect8.to_dictionary(), {'id': 15, 'width': 3, 'height': 2, 'x': 1, 'y': 2})

    def test_12(self):
        rect9 = Rectangle(10, 5, 0, 0, 14)
        self.assertEqual(rect9.id, 14)
        rect9.update(id=5)
        self.assertEqual(rect9.id, 5)

    def test_13(self):
        rect10 = Rectangle.create(**{'id': 89})
        self.assertEqual(rect10.id, 89)