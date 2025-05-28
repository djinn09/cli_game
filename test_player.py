import unittest
from unittest.mock import Mock, patch
from shooting_game import Player, Rifle, Deer # Import Deer or any Animal subclass for target

class TestPlayer(unittest.TestCase):
    """Test cases for the Player class."""
    def setUp(self):
        """Set up a Player instance and a Rifle instance before each test."""
        self.player = Player()
        self.rifle = Rifle() # Using Rifle as a concrete Gun implementation

    def test_choose_gun(self):
        """Test that choose_gun() correctly assigns the selected gun."""
        self.player.choose_gun(self.rifle)
        self.assertEqual(self.player.selected_gun, self.rifle, "Player should have the selected rifle.")

    def test_shoot_without_gun(self):
        """Test that shoot() does nothing if no gun is selected."""
        self.assertIsNone(self.player.selected_gun, "Player should have no gun selected initially.")
        # We can't directly assert that a print statement happened easily without more complex mocking,
        # so we'll ensure no points are added and no exceptions are raised.
        initial_points = self.player.points
        target_animal = Deer() # A concrete animal target
        self.player.shoot(target_animal)
        self.assertEqual(self.player.points, initial_points, "Points should not change if shooting without a gun.")

    @patch.object(Rifle, 'fire') # Mock the fire method of the Rifle class
    def test_shoot_with_gun_hit(self, mock_fire):
        """Test shoot() when the player has a gun and hits the target."""
        mock_fire.return_value = True # Simulate a hit
        
        # Create a mock target animal
        mock_target = Mock(spec=Deer) # Using Deer as a base, can be any Animal
        mock_target.get_shot.return_value = 10 # Points for hitting the target

        self.player.choose_gun(self.rifle) # Player selects the rifle
        initial_points = self.player.points
        
        self.player.shoot(mock_target) # Player shoots the mock target
        
        mock_fire.assert_called_once() # Ensure the gun's fire method was called
        mock_target.get_shot.assert_called_once() # Ensure the target's get_shot method was called
        self.assertEqual(self.player.points, initial_points + 10, "Player should gain points on a hit.")

    @patch.object(Rifle, 'fire') # Mock the fire method of the Rifle class
    def test_shoot_with_gun_miss(self, mock_fire):
        """Test shoot() when the player has a gun and misses the target."""
        mock_fire.return_value = False # Simulate a miss

        # Create a mock target animal
        mock_target = Mock(spec=Deer)

        self.player.choose_gun(self.rifle) # Player selects the rifle
        initial_points = self.player.points
        
        self.player.shoot(mock_target) # Player shoots the mock target
        
        mock_fire.assert_called_once() # Ensure the gun's fire method was called
        mock_target.get_shot.assert_not_called() # Ensure get_shot is not called on a miss
        self.assertEqual(self.player.points, initial_points, "Player's points should not change on a miss.")

    def test_add_points(self):
        """Test that add_points() correctly increases the player's points."""
        initial_points = self.player.points
        self.player.add_points(10)
        self.assertEqual(self.player.points, initial_points + 10, "Player's points should increase by the added amount.")
        self.player.add_points(5)
        self.assertEqual(self.player.points, initial_points + 15, "Player's points should be cumulative.")


if __name__ == '__main__':
    unittest.main()
