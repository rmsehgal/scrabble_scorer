import unittest
import board as sbd
import dictionary as sdi

class BoardTest(unittest.TestCase):
    def test_board_size_is_fifteen(self):
        bb = sbd.Board(15)
        self.assertEqual(bb.side_len(), 15)

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
            bb.add_word(pos, direct, wd, dd)

    def test_wrong_direction(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [0,0]
        wd = 'aa'
        direct = 'asdf'
        with self.assertRaises(ValueError):
            bb.add_word(pos, direct, wd, dd)

    def test_adding_word_outside_of_board(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [-1,2]
        wd = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.add_word(pos, direct, wd, dd)

    def test_adding_too_large_word(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [0,2]
        wd = '123456789'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb.add_word(pos, direct, wd, dd)

    def test_adding_first_word_correctly(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [2,2]
        wd = 'aa'
        direct = 'r'
        bb.add_word(pos, direct, wd, dd)
        self.assertEqual(bb.board,[['.']*5,['.']*5,['.','.','a','a','.'],['.']*5,['.']*5])

    def test_adding_second_word_not_ol(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [2,2]
        wd = 'aa'
        direct = 'd'
        bb.add_word(pos, direct, wd, dd)
        pos = [0,0]
        wd = 'aa'
        direct = 'd'
        with self.assertRaises(ValueError):
            bb.add_word(pos, direct, wd, dd)

    def test_adding_second_word_direct_ol(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa'])
        pos = [2,2]
        wd = 'aa'
        direct = 'r'
        bb.add_word(pos, direct, wd, dd)
        direct = 'd'
        bb.add_word(pos, direct, wd, dd)
        self.assertEqual(bb.board,[['.']*5,['.']*5,['.','.','a','a','.'],['.','.','a','.','.'],['.']*5])

    def test_adding_second_word_neighboring(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa','aaa'])
        pos = [2,2]
        wd = 'aa'
        direct = 'd'
        bb.add_word(pos, direct, wd, dd)
        pos = [2,3]
        bb.add_word(pos, direct, wd, dd)
        self.assertEqual(bb.board,[['.']*5,['.']*5,['.','.','a','a','.'],['.','.','a','a','.'],['.']*5])

    def test_adding_second_word_not_in_di(self):
        bb = sbd.Board(5)
        dd = sdi.Dictionary(['aa','ab'])
        pos = [2,2]
        wd = 'aa'
        direct = 'd'
        bb.add_word(pos, direct, wd, dd)
        pos = [2,1]
        wd = 'ab'
        direct = 'd'
        with self.assertRaises(ValueError):
            bb.add_word(pos, direct, wd, dd)

    def test_is_empty_exists(self):
        bb = sbd.Board(10)
        self.assertTrue(bb.is_empty)

if __name__ == '__main__':
    unittest.main()
