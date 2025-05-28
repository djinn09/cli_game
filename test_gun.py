import unittest
from unittest.mock import patch
from shooting_game import Rifle, Shotgun

class TestRifle(unittest.TestCase):
    """Test cases for the Rifle class."""
    def setUp(self):
        """Set up a Rifle instance before each test."""
        self.rifle = Rifle()

    @patch('random.random')
    def test_fire_hit(self, mock_random):
        """Test that fire() returns True when random.random() is less than 0.8 (hit)."""
        mock_random.return_value = 0.7 # Simulate a random value that results in a hit
        self.assertTrue(self.rifle.fire(), "Rifle should hit.")

    @patch('random.random')
    def test_fire_miss(self, mock_random):
        """Test that fire() returns False when random.random() is 0.8 or greater (miss)."""
        mock_random.return_value = 0.9 # Simulate a random value that results in a miss
        self.assertFalse(self.rifle.fire(), "Rifle should miss.")

class TestShotgun(unittest.TestCase):
    """Test cases for the Shotgun class."""
    def setUp(self):
        """Set up a Shotgun instance before each test."""
        self.shotgun = Shotgun()

    @patch('random.random')
    def test_fire_hit(self, mock_random):
        """Test that fire() returns True when random.random() is less than 0.5 (hit)."""
        mock_random.return_value = 0.4 # Simulate a random value that results in a hit
        self.assertTrue(self.shotgun.fire(), "Shotgun should hit.")

    @patch('random.random')
    def test_fire_miss(self, mock_random):
        """Test that fire() returns False when random.random() is 0.5 or greater (miss)."""
        mock_random.return_value = 0.6 # Simulate a random value that results in a miss
        self.assertFalse(self.shotgun.fire(), "Shotgun should miss.")


if __name__ == '__main__':
    unittest.main()
