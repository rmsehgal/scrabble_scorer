import unittest
import dictionary


class DictionaryTest(unittest.TestCase):
    def test_dictionary_contains_word(self):
        dd = dictionary.Dictionary(['aa','bb','11','22'])
        self.assertIn('aa', dd)
    def test_dictionary_does_not_contain_word(self):
        dd = dictionary.Dictionary(['aa','bb','11','22'])
        self.assertNotIn('qq', dd)



if __name__ == '__main__':
    unittest.main()

