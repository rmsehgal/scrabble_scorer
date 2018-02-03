import unittest
import Board

class BoardTest(unittest.TestCase):
    def test_board_size_is_fifteen(self):
        self.assertEqual(len(Board.board),15)
        self.assertEqual(len(Board.board[0]),15)

if __name__ == '__main__':
    unittest.main()
