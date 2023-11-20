import unittest
from shooting_game import Player, Rifle

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.rifle = Rifle()

    def test_choose_gun(self):
        self.player.choose_gun(self.rifle)
        self.assertEqual(self.player.selected_gun, self.rifle)

    def test_shoot_without_gun(self):
        self.assertIsNone(self.player.selected_gun)
        self.player.shoot(None)  # Assuming no effect when shooting without a gun

    def test_add_points(self):
        initial_points = self.player.points
        self.player.add_points(10)
        self.assertEqual(self.player.points, initial_points + 10)


if __name__ == '__main__':
    unittest.main()
