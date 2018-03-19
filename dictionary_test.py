"""
All tests written for dictionary function
"""
import unittest
import dictionary


class DictionaryTest(unittest.TestCase):
    """
    All tests for dictionary functions
    """
    def test_dict_contains_word(self):
        """
        Unit test to check that words are correctly in a dict
        """
        dd_test = dictionary.Dictionary(['aa', 'bb', '11', '22'])
        self.assertIn('aa', dd_test)
    def test_dict_does_not_contain_word(self):
        """
        Unit test to check that words are correctly id'ed as not in a dict
        """
        dd_test = dictionary.Dictionary(['aa', 'bb', '11', '22'])
        self.assertNotIn('qq', dd_test)



if __name__ == '__main__':
    unittest.main()

