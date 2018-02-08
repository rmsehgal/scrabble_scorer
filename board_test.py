import unittest
import board


class BoardTest(unittest.TestCase):
    def test_board_size_is_fifteen(self):
        bb = board.Board(15)
        self.assertEqual(bb.sideLen(), 15)


    def test_board_size_is_negative(self):
        with self.assertRaises(ValueError):
            board.Board(-1)


    # def test_adding_word_to_board(self):
    #     bb = board.Board(5)
    #     pos = [0,0]
    #     wd = 'aa'
    #     direct = 'down'
    #     bb.addWord(pos,direct,wd)



    def test_is_empty_exists(self):
        bb = board.Board(10)
        self.assertTrue(bb.is_empty)
        
if __name__ == '__main__':
    unittest.main()
