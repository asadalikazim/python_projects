'''A3. Tester for the function extract_mentions in tweets.
'''

import unittest
import tweets

class TestExtractMentions(unittest.TestCase):
    '''Tester for the function extract_mentions in tweets.
    '''

    def test_empty(self):
        '''Empty tweet.'''

        arg = ''
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)


    def test_nonempty_no_mention(self):
        '''Non-empty tweet with no mentions.'''

        arg = 'tweet test case 123 456 789 ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_nonempty_one_alpha_mention(self):
        '''Non-empty tweet with one alpha mention.'''

        arg = 'tweet @test case 123 456 789 ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)  
        
    def test_nonempty_more_than_alpha_mentions(self):
        '''Non-empty tweet with more than one alpha mentions.'''

        arg = '@tweet @test case 123 456 789 ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'test']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_one_numeric_mention(self):
        '''Non-empty tweet with one numeric mention.'''

        arg = 'tweet test case @123 456 789 ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['123']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_more_than_one_numeric_mention(self):
        '''Non-empty tweet with more than one numeric mentions.'''

        arg = 'tweet test case @123 @456 789 ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['123', '456']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_one_alphanumeric_mention(self):
        '''Non-empty tweet with one alphanumeric mentions.'''

        arg = 'tweet test case 123 456 789 @ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_nonempty_more_than_one_alphanumeric_mention(self):
        '''Non-empty tweet with more than one alphanumeric mentions.'''

        arg = 'tweet test case 123 456 789 @ab12 @cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['ab12', 'cd34']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_mixed_mentions(self):
        '''Non-empty tweet with mentions of differnet types'''
        
        arg = '@tweet test case @123 456 789 @ab12 cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', '123', 'ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
    
    def test_nonempty_multiple_repeated_mentions(self):
        '''Non-empty tweet with multiple repeated mentions'''
        
        arg = '@tweet @tweet @123 @123 @ab12 @ab12'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', 'tweet', '123', '123', 'ab12', 'ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_bad_trail_mentions(self):
        '''Non-empty tweet with mentions with trailing non-alphanumerics'''
        
        arg = '@tweet! test case @123? 456 789 @ab12% cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', '123', 'ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def test_nonempty_mixed_case_mentions(self):
        '''Non-empty tweet with mentions of mixed cases'''
        
        arg = '@tweET teST case @123 456 789 @Ab12 Cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', '123', 'ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg) 
        
    def test_nonempty_uppercase_mentions(self):
        '''Non-empty tweet with mentions of upper case'''
        
        arg = '@TWEET TEST case @123 456 789 @AB12 CD34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', '123', 'ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_nonempty_mixed_content(self):
        '''Non-empty tweet with mentions, hashtags and URL's'''
        
        arg = '@tweet #test case @123 #456 789 @ab12 http://cd34 ef56'
        actual = tweets.extract_mentions(arg)
        expected = ['tweet', '123', 'ab12']
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)   
        
    def test_nonempty_incorrect_mentions(self):
        '''Non-empty tweet with incorrect mention formats'''
        
        arg = '@ @!a @!1 @@! @@a @@1'
        actual = tweets.extract_mentions(arg)
        expected = []
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)      


if __name__ == '__main__':
    unittest.main(exit=False)
