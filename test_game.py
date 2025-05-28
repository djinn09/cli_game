import unittest
from unittest.mock import patch, MagicMock
from shooting_game import Game, Player, ScoreBoard, Rifle, Shotgun, Deer, Bear, Animal, Gun

class TestGame(unittest.TestCase):
    """Test cases for the Game class."""

    def setUp(self):
        """Set up a Game instance before each test."""
        self.game = Game()

    def test_init(self):
        """Test that the Game initializes with correct default attributes."""
        self.assertIsInstance(self.game.player, Player, "Game should initialize with a Player instance.")
        self.assertIsInstance(self.game.scoreboard, ScoreBoard, "Game should initialize with a ScoreBoard instance.")
        self.assertIsInstance(self.game.animals, list, "Game animals should be a list.")
        self.assertTrue(all(isinstance(animal, Animal) for animal in self.game.animals), "All items in animals list should be Animal instances.")
        self.assertGreater(len(self.game.animals), 0, "Animals list should not be empty.")
        self.assertIsInstance(self.game.guns, list, "Game guns should be a list.")
        self.assertTrue(all(isinstance(gun, Gun) for gun in self.game.guns), "All items in guns list should be Gun instances.")
        self.assertGreater(len(self.game.guns), 0, "Guns list should not be empty.")
        self.assertFalse(self.game.is_game_running, "Game should initially not be running.")

    @patch('builtins.input')
    def test_choose_gun_from_list_valid_choice(self, mock_input):
        """Test choose_gun_from_list with a valid user input."""
        # Simulate user choosing the first gun
        mock_input.return_value = '1'
        chosen_gun = self.game.choose_gun_from_list()
        self.assertEqual(chosen_gun, self.game.guns[0], "Should return the first gun for input '1'.")

    @patch('builtins.input')
    def test_choose_gun_from_list_invalid_choice_then_valid(self, mock_input):
        """Test choose_gun_from_list with an invalid then a valid user input."""
        # Simulate user entering an out-of-range number, then '1'
        mock_input.side_effect = ['0', '1'] # First input invalid, second valid
        
        # First call with '0' should return None (or handle error and ask again, depending on implementation)
        # The current implementation prints an error and returns None for invalid numeric choice
        # We'll directly test the return for the first invalid input if the game is structured to return immediately
        # However, start_game loop until a valid gun is chosen.
        # So we check the final outcome after a valid choice.
        
        # To test the scenario properly as per current game logic, we'd need to simulate the loop in start_game
        # For this unit test, we focus on choose_gun_from_list's direct behavior.
        # It will print "Invalid Choice..." and return None for '0'
        # The test needs to reflect what choose_gun_from_list actually returns.
        
        # Test first invalid input
        chosen_gun_invalid = self.game.choose_gun_from_list() 
        self.assertIsNone(chosen_gun_invalid, "Should return None for out-of-range input '0'.")
        
        # Test subsequent valid input
        chosen_gun_valid = self.game.choose_gun_from_list()
        self.assertEqual(chosen_gun_valid, self.game.guns[0], "Should return the first gun for input '1' after an invalid attempt.")


    @patch('builtins.input')
    def test_choose_gun_from_list_non_numeric_choice(self, mock_input):
        """Test choose_gun_from_list with a non-numeric user input."""
        # Simulate user entering a non-numeric value
        mock_input.return_value = 'abc'
        chosen_gun = self.game.choose_gun_from_list()
        self.assertIsNone(chosen_gun, "Should return None for non-numeric input.")

    @patch('builtins.input', return_value='1') # User input is '1'
    @patch('builtins.print') # Mock print to suppress output and check calls
    def test_choose_gun_from_list_unexpected_exception(self, mock_print, mock_input):
        """Test choose_gun_from_list for handling an unexpected exception during gun access."""
        original_guns = self.game.guns
        
        # Create a mock for self.game.guns that will behave mostly like a list
        # but will raise a specific error when a particular operation is performed.
        mock_guns_list = MagicMock(spec=list) 
        
        # Configure len() to return a value that allows the choice '1' to be in range.
        # Choice '1' means index 0. So len must be at least 1.
        mock_guns_list.__len__.return_value = 1 
        
        # Configure the __getitem__ method (used for indexing like self.guns[choice - 1])
        # to raise a TypeError. This is the unexpected error we want to trigger.
        expected_error_message = "Simulated unexpected error during gun access"
        mock_guns_list.__getitem__.side_effect = TypeError(expected_error_message)
        
        # Temporarily replace self.game.guns with our configured mock
        self.game.guns = mock_guns_list
        
        chosen_gun = self.game.choose_gun_from_list()
        
        self.assertIsNone(chosen_gun, "Should return None when an unexpected exception occurs.")
        
        # Check that the specific error message was printed.
        # The print call in the source is print(f"An unexpected error occurred: {e}")
        mock_print.assert_any_call(f"An unexpected error occurred: {expected_error_message}")
        
        # Restore the original guns list to avoid affecting other tests
        self.game.guns = original_guns

    @patch('random.choice')
    def test_random_animal(self, mock_random_choice):
        """Test that random_animal returns an animal from the game's animal list."""
        # Have random.choice return the first animal in the list
        mock_random_choice.return_value = self.game.animals[0]
        chosen_animal = self.game.random_animal()
        self.assertIn(chosen_animal, self.game.animals, "Chosen animal should be in the game's list of animals.")
        self.assertEqual(chosen_animal, self.game.animals[0], "Should return the animal mocked by random.choice.")

    @patch('shooting_game.Game.display_score') # Mocking display_score method of Game
    def test_end_game(self, mock_display_score):
        """Test that end_game sets is_game_running to False and calls display_score."""
        self.game.is_game_running = True # Start the game first
        self.game.end_game()
        self.assertFalse(self.game.is_game_running, "is_game_running should be False after ending the game.")
        mock_display_score.assert_called_once() # Check if display_score was called

    @patch('shooting_game.Game.choose_gun_from_list')
    @patch('shooting_game.Player.choose_gun')
    @patch('shooting_game.Game.game_loop')
    def test_start_game_flow(self, mock_game_loop, mock_player_choose_gun, mock_choose_gun_from_list):
        """Test the initial flow of start_game up to calling game_loop."""
        # Simulate choose_gun_from_list returning a valid gun (e.g., the first one)
        mock_gun = self.game.guns[0]
        mock_choose_gun_from_list.return_value = mock_gun
        
        self.game.start_game()
        
        self.assertTrue(self.game.is_game_running, "Game should be running after start_game.")
        mock_choose_gun_from_list.assert_called() # Ensure gun selection was attempted
        mock_player_choose_gun.assert_called_with(mock_gun) # Ensure player was given the gun
        mock_game_loop.assert_called_once() # Ensure the game loop was started

    @patch('builtins.input')
    @patch('shooting_game.Game.display_options')
    @patch('shooting_game.Player.shoot')
    @patch('shooting_game.Game.random_animal')
    # Mock end_game to prevent it from trying to call display_score during this specific test if not desired
    @patch('shooting_game.Game.end_game')
    def test_game_loop_shoot_then_end_action(self, mock_end_game, mock_random_animal, mock_player_shoot, mock_display_options, mock_input):
        """Test the game_loop for 'shoot' action followed by 'end game' action."""
        # Simulate: 1. User chooses '1' (shoot), 2. User chooses '2' (end game) to exit loop
        mock_input.side_effect = ['1', '2']

        # Mock random_animal to return a predictable animal
        mock_animal_instance = Deer() # Using a concrete instance for simplicity
        mock_random_animal.return_value = mock_animal_instance

        # Define the side effect for mock_end_game to also stop the game loop
        def end_game_side_effect():
            self.game.is_game_running = False
        mock_end_game.side_effect = end_game_side_effect

        # Start the game loop
        self.game.is_game_running = True
        self.game.game_loop()

        # Assertions
        # display_options is called once for 'shoot' and once for 'end game' prompt
        self.assertEqual(mock_display_options.call_count, 2, "display_options should be called for each action prompt.")
        # random_animal is called once for the 'shoot' action
        mock_random_animal.assert_called_once()
        # player.shoot is called with the chosen animal
        mock_player_shoot.assert_called_with(mock_animal_instance)
        # end_game is called once when user inputs '2'
        mock_end_game.assert_called_once()
        # The game loop should terminate, so is_game_running should be False
        self.assertFalse(self.game.is_game_running, "is_game_running should be False after 'end game' action.")

    @patch('shooting_game.Game') # Mock the Game class where it's defined in shooting_game module
    @patch('builtins.input')    # Mock input to prevent actual game interaction
    def test_main_function_calls_game_start(self, mock_input, MockedGame):
        """Test that the main() function in shooting_game.py instantiates Game and calls start_game()."""
        # Import the module that contains the main() function
        import shooting_game 
        
        # Configure the mock Game class (MockedGame) so that when Game() is called,
        # it returns a specific mock instance.
        mock_game_instance = MagicMock()
        MockedGame.return_value = mock_game_instance

        # Provide default input for any input() calls within the game logic that might run.
        # Though start_game is mocked, other parts might still prompt for input.
        mock_input.side_effect = ['1', '2'] # Example: '1' for gun choice, '2' to end game.

        # Call the main() function from the shooting_game module.
        shooting_game.main()
            
        # Assert that Game() was instantiated (i.e., MockedGame was called).
        MockedGame.assert_called_once()
        # Assert that start_game() was called on the instance returned by Game().
        mock_game_instance.start_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()
