"""All unit tests for board class"""
import unittest
import board as sbd
import dictionary as sdi

class BoardTest(unittest.TestCase):
    """All unit tests for board class"""
    def test_board_size_is_fifteen(self):
        """
        Unit test to ensure that a board is the size we think it is
        """
        bb_test = sbd.Board(15)
        self.assertEqual(bb_test.side_len(), 15)

    def test_board_size_is_negative(self):
        """
        Unit test to ensure board size is >0
        """
        with self.assertRaises(ValueError):
            sbd.Board(-1)

    def test_add_first_word_to_board(self):
        """
        Unit test for add first word to board
        not in center
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [0, 0]
        wd_test = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb_test.add_word(pos, direct, wd_test, dd_test)

    def test_wrong_direction(self):
        """
        Unit test to check that direction is
        well posed
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [0, 0]
        wd_test = 'aa'
        direct = 'asdf'
        with self.assertRaises(ValueError):
            bb_test.add_word(pos, direct, wd_test, dd_test)

    def test_add_word_out_of_board(self):
        """
        Unit test to check that position
        is within the board
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [-1, 2]
        wd_test = 'aa'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb_test.add_word(pos, direct, wd_test, dd_test)

    def test_add_too_large_word(self):
        """
        Unit test to check that a word can
        fit on the board
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [0, 2]
        wd_test = '123456789'
        direct = 'down'
        with self.assertRaises(ValueError):
            bb_test.add_word(pos, direct, wd_test, dd_test)

    def test_add_first_word(self):
        """
        Unit test to add first word correctly
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [2, 2]
        wd_test = 'aa'
        direct = 'r'
        bb_test.add_word(pos, direct, wd_test, dd_test)
        self.assertEqual(bb_test.board,
                         [['.']*5,
                          ['.']*5,
                          ['.', '.', 'a', 'a', '.'],
                          ['.']*5,
                          ['.']*5])
    def test_add_second_word_not_ol(self):
        """
        Unit test that checks if second word added
        is not overlapped with words on board
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [2, 2]
        wd_test = 'aa'
        direct = 'd'
        bb_test.add_word(pos, direct, wd_test, dd_test)
        pos = [0, 0]
        wd_test = 'aa'
        direct = 'd'
        with self.assertRaises(ValueError):
            bb_test.add_word(pos, direct, wd_test, dd_test)
    def test_add_second_word_dir_ol(self):
        """
        Unit test that checks that a word overlapped
        correctly
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa'])
        pos = [2, 2]
        wd_test = 'aa'
        direct = 'r'
        bb_test.add_word(pos, direct, wd_test, dd_test)
        direct = 'd'
        bb_test.add_word(pos, direct, wd_test, dd_test)
        self.assertEqual(bb_test.board,
                         [['.']*5,
                          ['.']*5,
                          ['.', '.', 'a', 'a', '.'],
                          ['.', '.', 'a', '.', '.'],
                          ['.']*5])
    def test_add_second_word_neigh(self):
        """
        Unit tests for adding a word which
        neighbors but doesn't overlap
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa', 'aaa'])
        pos = [2, 2]
        wd_test = 'aa'
        direct = 'd'
        bb_test.add_word(pos, direct, wd_test, dd_test)
        pos = [2, 3]
        bb_test.add_word(pos, direct, wd_test, dd_test)
        self.assertEqual(bb_test.board,
                         [['.']*5,
                          ['.']*5,
                          ['.', '.', 'a', 'a', '.'],
                          ['.', '.', 'a', 'a', '.'],
                          ['.']*5])
    def test_add_second_word_not_in_di(self):
        """
        Unit test to check what happens if by adding
        a second word we form a word not in dict/lexic
        """
        bb_test = sbd.Board(5)
        dd_test = sdi.Dictionary(['aa', 'ab'])
        pos = [2, 2]
        wd_test = 'aa'
        direct = 'd'
        bb_test.add_word(pos, direct, wd_test, dd_test)
        pos = [2, 1]
        wd_test = 'ab'
        direct = 'd'
        with self.assertRaises(ValueError):
            bb_test.add_word(pos, direct, wd_test, dd_test)
    def test_is_empty_exists(self):
        """
        Unit test to check if board is
        empty works correctly
        """
        bb_test = sbd.Board(10)
        self.assertTrue(bb_test.is_empty)

if __name__ == '__main__':
    unittest.main()
