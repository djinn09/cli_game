import unittest
from unittest.mock import patch
import io # For capturing print output
from shooting_game import ScoreBoard

class TestScoreBoard(unittest.TestCase):
    """Test cases for the ScoreBoard class."""
    def setUp(self):
        """Set up a ScoreBoard instance before each test."""
        self.scoreboard = ScoreBoard()

    def test_update_score(self):
        """Test that update_score correctly updates total_score and score_history."""
        self.scoreboard.update_score(10)
        self.assertEqual(self.scoreboard.total_score, 10, "Total score should be 10 after adding 10.")
        self.assertEqual(self.scoreboard.score_history, [10], "Score history should contain [10].")

        self.scoreboard.update_score(5)
        self.assertEqual(self.scoreboard.total_score, 15, "Total score should be 15 after adding 5 more.")
        self.assertEqual(self.scoreboard.score_history, [10, 5], "Score history should be [10, 5].")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_score(self, mock_stdout):
        """Test that display_score prints the current total score and score history correctly."""
        self.scoreboard.update_score(15)
        self.scoreboard.update_score(5)
        
        # The update_score method also prints. This output will be part of mock_stdout.getvalue().
        # Output from update_score(15): "Score updated: +15 points\n"
        # Output from update_score(5): "Score updated: +5 points\n"
        
        # Expected output from display_score() itself:
        # Current Score: 20
        # Score History:
        #   +15 points
        #   +5 points
        
        self.scoreboard.display_score()
        
        # The full expected output in mock_stdout should include prints from update_score
        expected_output_from_updates = "Score updated: +15 points\nScore updated: +5 points\n"
        expected_output_from_display = "Current Score: 20\nScore History:\n  +15 points\n  +5 points\n"
        full_expected_output = expected_output_from_updates + expected_output_from_display
        
        self.assertEqual(mock_stdout.getvalue(), full_expected_output, "Output of display_score (including previous prints) is not as expected.")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_score_empty(self, mock_stdout):
        """Test display_score when there is no score history."""
        self.scoreboard.display_score()
        expected_output = "Current Score: 0\nScore History:\n" # History will be empty
        self.assertEqual(mock_stdout.getvalue(), expected_output, "Output of display_score for empty scoreboard is not as expected.")


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_final_score(self, mock_stdout):
        """Test that display_final_score prints the final total score correctly."""
        self.scoreboard.total_score = 100 # Directly set for testing final display
        
        self.scoreboard.display_final_score()
        expected_output = "Final Score: 100\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output, "Output of display_final_score is not as expected.")

# Add more tests as needed

if __name__ == '__main__':
    unittest.main()
