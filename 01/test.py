"""Module for test"""
import unittest

from tictac import TicTacGame


class Test(unittest.TestCase):
    """Test class"""
    def setUp(self):
        self.game = TicTacGame()

    def test_init_game(self):
        """Test init board for game"""
        self.assertEqual(len(self.game.field), 9)

    def test_player_pick(self):
        """Test filling field by player"""
        self.game.player_pick(cell=5)
        self.assertEqual(self.game.field[4], 1)

    def test_computer_pick(self):
        """Test filling fiend by computer"""
        self.game.computer_pick()
        self.assertEqual(len(list(filter(lambda x: x == 2, self.game.field))), 1)

    def test_win(self):
        """Test win mask"""
        self.game.player_pick(cell=1)
        self.game.player_pick(cell=2)
        self.game.player_pick(cell=3)
        self.assertTrue(self.game.check_winner('Игрок'))


if __name__ == "__main__":
    unittest.main()
