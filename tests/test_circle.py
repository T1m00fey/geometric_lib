import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(area(2), 12.566370614359172)

    def test_area_zero(self):
        self.assertAlmostEqual(area(0), 0)

    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(2), 12.566370614359172)

    def test_perimeter_zero(self):
        self.assertAlmostEqual(perimeter(0), 0)


if __name__ == '__main__':
    unittest.main()