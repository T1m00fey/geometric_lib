import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        result = area(3, 4)
        self.assertEqual(result, 12)

    def test_area_zero(self):
        result = area(10, 0)
        self.assertEqual(result, 0)

    def test_perimeter(self):
        result = perimeter(3, 4)
        self.assertEqual(result, 14)

    def test_perimeter_zero(self):
        result = perimeter(0, 5)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()