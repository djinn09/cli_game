import unittest
from shooting_game import ScoreBoard

class TestScoreBoard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = ScoreBoard()

    def test_update_score(self):
        self.scoreboard.update_score(10)
        self.assertEqual(self.scoreboard.total_score, 10)
        self.assertIn(10, self.scoreboard.score_history)


# Add more tests as needed

if __name__ == '__main__':
    unittest.main()
