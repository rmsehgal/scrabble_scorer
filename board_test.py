import unittest
import board as sbd
import dictionary as sdi

class BoardTest(unittest.TestCase):
    def test_board_size_is_fifteen(self):
        bb = sbd.Board(15)
        self.assertEqual(bb.sideLen(), 15)

    def test_board_size_is_negative(self):
        with self.assertRaises(ValueError):
            sbd.Board(-1)

    def test_adding_first_word_to_board(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [0,0]
        wd = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd,dd)

    def test_wrong_direction(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [0,0]
        wd = 'aa'
        direct = 'asdf'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd,dd)
            
    def test_adding_word_outside_of_board(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [-1,2] 
        wd = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd,dd)
            
    def test_adding_too_large_word(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [0,2] 
        wd = '123456789'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.addWord(pos,direct,wd,dd)

    def test_adding_first_word_correctly(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [2,2]
        wd = 'aa'
        direct = 'r'
        bb.addWord(pos,direct,wd,dd)
        self.assertEqual(bb.board,[['.']*5,['.']*5,['.','.','a','a','.'],['.']*5,['.']*5])

            
        
    def test_isEmpty_exists(self):
        bb = sbd.Board(10)
        self.assertTrue(bb.isEmpty)
        
if __name__ == '__main__':
    unittest.main()
