import unittest
from shooting_game import Deer, Bear

class TestDeer(unittest.TestCase):
    def setUp(self):
        self.deer = Deer()

    def test_get_shot(self):
        points = self.deer.get_shot()
        self.assertEqual(points, 10)

class TestBear(unittest.TestCase):
    def setUp(self):
        self.bear = Bear()

    def test_get_shot(self):
        points = self.bear.get_shot()
        self.assertEqual(points, 20)


if __name__ == '__main__':
    unittest.main()
