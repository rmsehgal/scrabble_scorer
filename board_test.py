import unittest
import board

class BoardTest(unittest.TestCase):
    def test_board_size_is_fifteen(self):
        bb = board.Board(15)
        self.assertEqual(bb.sideLen(),15)

if __name__ == '__main__':
    unittest.main()
