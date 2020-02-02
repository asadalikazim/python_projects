'''A3. Tester for the function common_words in tweets.
'''

import unittest
import tweets

class TestCommonWords(unittest.TestCase):
    '''Tester for the function common_words in tweets.
    '''

    def test_empty(self):
        '''Empty dictionary.'''

        arg1 = {}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be\n {}, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)


    def test_one_word_limit_one(self):
        '''Dictionary with one word.'''

        arg1 = {'hello': 2}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_two_word_limit_one(self):
        '''Dictionary with two words and binding word limit.'''

        arg1 = {'hello': 2, 'bye': 1}
        arg2 = 1
        exp_arg1 = {'hello': 2}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_non_binding_word_limit(self):
        '''Dictionary with words less than the word limit resulting in no change
        in the dictionary'''

        arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7, 'f': 6}
        arg2 = 10
        exp_arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7, 'f': 6}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
        
    def test_non_affecting_tied_counts(self):
        '''Dictionary with words with tied counts but still
        len(exp_arg1) == arg2.'''

        arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7, 'f': 6}
        arg2 = 5
        exp_arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
        
    def test_non_affecting_tied_counts_border_case(self):
        '''Dictionary with words with same counts but still 
        len(exp_arg1) == arg2.'''

        arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7, 'f': 6}
        arg2 = 4
        exp_arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)
        
    def test_affecting_tied_counts(self):
        '''Dictionary with words with tied counts and 
        len(exp_arg1) < arg2.'''

        arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7, 'f': 6}
        arg2 = 3
        exp_arg1 = {'a': 9, 'b': 9}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    
    
    def test_affecting_tied_counts_extreme_case(self):
        '''Dictionary with words with tied counts resulting in an empty
        dictionary.''' 
        
        arg1 = {'a': 9, 'b': 9, 'c': 8, 'd': 8, 'e': 7, 'f': 6}
        arg2 = 1
        exp_arg1 = {}
        act_return = tweets.common_words(arg1, arg2)
        exp_return = None

        msg = "Expected {}, but returned {}".format(exp_return, act_return)
        self.assertEqual(act_return, exp_return, msg)

        msg = ("Expected dictionary to be {}\n, " +
               "but it was\n {}").format(exp_arg1, arg1)
        self.assertEqual(arg1, exp_arg1, msg)    


if __name__ == '__main__':
    unittest.main(exit=False)
