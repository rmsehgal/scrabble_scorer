import unittest
import board


class BoardTest(unittest.TestCase):
    def test_board_size_is_fifteen(self):
        bb = board.Board(15)
        self.assertEqual(bb.sideLen(), 15)

    def test_board_size_is_negative(self):
        with self.assertRaises(ValueError):
            board.Board(-1)

    def test_adding_first_word_to_board(self):
        bb = board.Board(5)
        pos = [0,0]
        wd = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd)

    def test_wrong_direction(self):
        bb = board.Board(5)
        pos = [0,0]
        wd = 'aa'
        direct = 'asdf'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd)
            
    def test_adding_word_outside_of_board(self):
        bb = board.Board(5)
        pos = [-1,2] 
        wd = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd)
            
    def test_adding_too_large_word(self):
        bb = board.Board(5)
        pos = [0,2] 
        wd = '123456789'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd)

    def test_isEmpty_exists(self):
        bb = board.Board(10)
        self.assertTrue(bb.isEmpty)
        
if __name__ == '__main__':
    unittest.main()
