import unittest
from shooting_game import Rifle, Shotgun

class TestRifle(unittest.TestCase):
    def setUp(self):
        self.rifle = Rifle()

    

class TestShotgun(unittest.TestCase):
    def setUp(self):
        self.shotgun = Shotgun()




if __name__ == '__main__':
    unittest.main()
