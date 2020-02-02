"""Assignment 3: Tweet Analysis"""

from typing import List, Dict, TextIO, Tuple

HASH_SYMBOL = '#'
MENTION_SYMBOL = '@'
URL_START = 'http'

# Order of data in the file
FILE_DATE_INDEX = 0
FILE_LOCATION_INDEX = 1
FILE_SOURCE_INDEX = 2
FILE_FAVOURITE_INDEX = 3
FILE_RETWEET_INDEX = 4

# Order of data in a tweet tuple
TWEET_TEXT_INDEX = 0
TWEET_DATE_INDEX = 1
TWEET_SOURCE_INDEX = 2
TWEET_FAVOURITE_INDEX = 3
TWEET_RETWEET_INDEX = 4

# Helper functions.

def alnum_prefix(text: str) -> str:
    """Return the alphanumeric prefix of text, converted to
    lowercase. That is, return all characters in text from the
    beginning until the first non-alphanumeric character or until the
    end of text, if text does not contain any non-alphanumeric
    characters.

    >>> alnum_prefix('')
    ''
    >>> alnum_prefix('IamIamIam')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!')
    'iamiamiam'
    >>> alnum_prefix('IamIamIam!!andMore')
    'iamiamiam'
    >>> alnum_prefix('$$$money')
    ''

    """

    index = 0
    while index < len(text) and text[index].isalnum():
        index += 1
    return text[:index].lower()


def clean_word(word: str) -> str:
    """Return all alphanumeric characters from word, in the same order as
    they appear in word, converted to lowercase.

    >>> clean_word('')
    ''
    >>> clean_word('AlreadyClean?')
    'alreadyclean'
    >>> clean_word('very123mes$_sy?')
    'very123messy'

    """

    cleaned_word = ''
    for char in word.lower():
        if char.isalnum():
            cleaned_word = cleaned_word + char
    return cleaned_word


# Required functions

def extract_mentions(text: str) -> List[str]:
    """Return a list of all mentions in text, converted to lowercase, with
    duplicates included.

    >>> extract_mentions('Hi @UofT do you like @cats @CATS #meowmeow')
    ['uoft', 'cats', 'cats']
    >>> extract_mentions('@cats are #cute @cats @cat meow @meow')
    ['cats', 'cats', 'cat', 'meow']
    >>> extract_mentions('@many @cats$extra @meow?!')
    ['many', 'cats', 'meow']
    >>> extract_mentions('No valid mentions @! here?')
    []

    """

    # TODO: complete this function body
    
    lst1 = text.split()
    result = []
    for word in lst1:
        if word[0] == MENTION_SYMBOL and len(word) > 1:
            mention = alnum_prefix(word[1:])
            if mention != '':
                result.append(mention)
    return result


# TODO: Add the remaining Assignment 3 functions below.
def extract_hashtags(text: str) -> List[str]:
    """Return a list of only the first occurences of a hashtag in the text,
    converted to lowercase, and being case insensitive, and also in the 
    order in which they appear in the text.
    
    >>> extract_hashtags('Hi #UofT do you like #cats #CATS #meowmeow')
    ['uoft', 'cats', 'meowmeow']
    >>> extract_hashtags('#cats are #cute #cats #cat meow @meow')
    ['cats', 'cute', 'cat']
    >>> extract_hashtags('#many #cats$extra #meow?!')
    ['many', 'cats', 'meow']
    >>> extract_hashtags('No valid hashtags #! here?')
    []
    """
    
    lst1 = text.split()
    result = []
    for word in lst1:
        if word[0] == HASH_SYMBOL and len(word) > 1:
            hashtag = alnum_prefix(word[1:])
            if hashtag != '' and hashtag not in result:
                result.append(hashtag)
    return result
    
def count_words(text: str, my_dict: Dict[str, int]) -> None:
    """my_dict is a dictionary with words as keys, and the corresponding value
    is the count of that word in tweets. For each word in text increase its 
    count in my_dict appropriately. If a new word is encountered, include it in 
    my_dict from scratch. While considering a word be case insensitive,
    only consider alphanumeric characters and do not consider hashtags,
    mentions, or URL's.
    
    >>>my_dict = {}
    >>>count_words("ooga booga ooga2 booga2", my_dict)
    >>>my_dict == {"ooga": 1, "booga": 1, "ooga2": 1, "booga2": 1}
    True
    
    >>>my_dict = { "ola": 5}
    >>>count_words("ol-a ol!a ol%a", my_dict)
    >>>my_dict == {"ola": 8}
    True
    
    >>>my_dict = {"ola": 5}
    >>>count_words("@ola #ola https://ola.com", my_dict)
    >>>my_dict == {"ola": 5}
    True
    
    >>>my_dict = {}
    >>>count_words("", my_dict)
    >>>my_dict == {}
    True
    """
    
    lst1 = text.split()
    lst2 = only_words(lst1)
    for word in lst2:
        if word in my_dict:
            my_dict[word] += 1
        else:
            my_dict[word] = 1
    
            
    
    
def only_words(lst1: List[str]) -> List[str]:
    """Returns a list with only items that are considered words in twitter, 
    without non-alphanumeric characters, and lower cased. Removes mentions, 
    hashtags, and URL's.
    
    >>>only_words(['Alohamora!', 'Lumos!', '#crucio', 'http:avada_kedavra.com',\
    '@imperio'])
    ['alohamora', 'lumos']
    """
    
    result = []
    for word in lst1:
        if word[0] != HASH_SYMBOL and word[0] != MENTION_SYMBOL and \
           not word.startswith(URL_START):
            result.append(clean_word(word))
    return result
    
def common_words(my_dict: Dict[str, int], n: int) -> None:
    """my_dict is a dicitionary of words and their counts. Modify my_dict in
    such a way that at most N words are left in it such that these were the 
    words with the highest counts in my_dict. Ignore all ties that would lead to
    the words in my_dict being more than N.
    
    Precondition: n > 0
    
    >>>my_dict = {'a': 6, 'b': 5, 'c': 4}
    >>>common_words(my_dict, 1)
    >>>my_dict == {'a': 6}
    True
    
    >>>my_dict = {'a': 6, 'b': 5, 'c': 5}
    >>>common_words(my_dict, 2)
    >>>my_dict == {'a': 6}
    True
    
    >>>my_dict = {'a': 5, 'b': 5, 'c': 5}
    >>>common_words(my_dict, 1)
    >>>my_dict == {}
    True
    """
    if len(my_dict) > n: #if there are <= n words in my_dict, we are done
        #create a helper list containing all the word  and counts of my_dict
        lst1 = []
        lst2 = []
        for word in my_dict:
            lst1.append(my_dict[word])
            lst2.append(word)
        
        #sort the list in descending order
        lst1.sort()
        lst1 = lst1[::-1]
        
        #make the length of the list <= N
        if lst1[n-1] != lst1[n]:
            lst1 = lst1[:n]
        else:
            i = 0
            while lst1[i] != lst1[n-1]:
                i += 1
            lst1 = lst1[:i]
            
        #remove the words that do not have counts appearing in helper list
        for word in lst2:
            if my_dict[word] not in lst1:
                del my_dict[word]
    
def read_tweets(file: TextIO) -> Dict[str, List[tuple]]:
    """file is of the format outlined in the handout. this function creates a 
    dict of the format outlined in the handout from file.
    
    Precondition: first line of file has to be a user name
    """
    
    d = {}  #final dict to be returned
    
    maj_lst = file.readlines()
    file.close()
    
    i = 0
    while i < len(maj_lst):
        if maj_lst[i][-2] == ':' and " " not in maj_lst[i]:
            current_user = maj_lst[i][:-2].lower()
            d[current_user] = []
        else:
            lst = get_tweet(maj_lst, i)
            d[current_user].append(lst[0])
            i = lst[1]
        i += 1
        
    return d

def get_tweet(lst1: List[str], j: int) -> tuple:
    """lst1 is a list generated as a result of performing the readlines() method
    on the data file for this assignment. This function returns a completely 
    formatted tweet, the first one it encounters from index j in lst1, as a
    tuple of format=> (tweet text, date, source, favourite count, retweet count)
    and the progress in index.
    
    >>>get_tweet(["user1:\n", "98765,location,source,0,0\n", "text\n", \
    "<<<EOT\n", "54321,location,source,1,1\n", "text2\n","user2:\n"], 1)
    [("text",98765,"source", 0, 0), 3]
    """
    
    tweet = [0, 0, 0, 0, 0]  #dummy parallel of the tuple to be returned
    
    basic_data = lst1[j][:-1] #removes the newline character from basic data
    lst2 = basic_data.split(",") 
    
    tweet[TWEET_DATE_INDEX] = int(lst2[FILE_DATE_INDEX])
    tweet[TWEET_SOURCE_INDEX] = lst2[FILE_SOURCE_INDEX]
    tweet[TWEET_FAVOURITE_INDEX] = int(lst2[FILE_FAVOURITE_INDEX])
    tweet[TWEET_RETWEET_INDEX] = int(lst2[FILE_RETWEET_INDEX])
    
    j += 1
    
    lst3 = get_tweet_text(lst1, j)
    tweet[TWEET_TEXT_INDEX] = lst3[0]
    
    return [(tweet[0], tweet[1], tweet[2], tweet[3], tweet[4]), lst3[1]]

def get_tweet_text(lst1: List[str], k: int) -> str:
    """lst1 is a list generated as a result of performing the readlines() method
    on the data file for this assignment. this function returns the text of a 
    single tweet starting at index k, with trailing and leading whitespace
    removed, and the progress in index.
    
    >>>get_tweet_text(["user1:\n", "98765,location,source,0,0\n", "text\n", \
    "more text    \n", "<<<EOT\n", "54321,location,source,1,1\n", "text2\n", \
    "user2:\n"], 2)
    ["text more text", 4]
    """
    text = ""
    while lst1[k] != "<<<EOT\n":
        if lst1[k] != "\n":
            text = text + lst1[k][:-1]
        k += 1
    return [text.strip(), k]

def most_popular(d: Dict[str, List[tuple]], small: int, big: int) -> str:
    """returns the most popular user on twitter between the dates small and big,
    and 'tie' if more than one users equal in popularity, or no users in the 
    specified dates. popularity of a tweet depends on the sum of favorites and 
    retweets. Most popular user is the user with the most popular tweet.
    d is the output of read_tweets
    
    Precondition: small <= big
    
    >>>most_popular({'user1': [('txt', 10, 'src1', 5, 5), ('txt', 5, 'src1', 5,\
    5)], 'user2': [('txt', 8, 'src2', 7, 7)]}, 5, 10)
    'user2'
    
    >>>most_popular({'user1': [('txt', 10, 'src1', 5, 5), ('txt', 5, 'src1', 5,\
    5)], 'user2': [('txt', 8, 'src2', 7, 7)]}, 5, 6)
    'user1'
    
    >>>most_popular({'user1': [('txt', 10, 'src1', 5, 5), ('txt', 5, 'src1', 5,\
    5)], 'user2': [('txt', 8, 'src2', 7, 7)]}, 3, 4)
    'tie'
    
    >>>most_popular({'user1': [('txt', 10, 'src1', 7, 7), ('txt', 5, 'src1', 5,\
    5)], 'user2': [('txt', 8, 'src2', 7, 7)]}, 5, 10)
    'tie'
    """
    
    pop_user = 'tie'
    pop_count = -1
    
    for user in d:
        for tweet in d[user]:
            if small <= tweet[TWEET_DATE_INDEX] <= big:
                if tweet[TWEET_FAVOURITE_INDEX] + tweet[TWEET_RETWEET_INDEX] > \
                   pop_count:
                    pop_user = user
                    pop_count = tweet[TWEET_FAVOURITE_INDEX] + \
                        tweet[TWEET_RETWEET_INDEX]
                elif tweet[TWEET_FAVOURITE_INDEX] + tweet[TWEET_RETWEET_INDEX] \
                   == pop_count and pop_user != user:
                    pop_user = 'tie'
    return pop_user
        
def detect_author(d: Dict[str, List[tuple]], text: str) -> str:
    """d is the the output of read_tweets. this function returns the original 
    author of the tweet text, depending on whether all the hashtags in text
    have been used uniquely by a user in d, else it returns 'unknown'
    
    >>>detect_author({'user1': [('#cat #dog fight',1,'1',1,1), \
    ('yolo',1,'1',1,1)], 'user2': [('#cat',1,'1',1,1)]}, '#cat')
    'unknown'
    
    >>>detect_author({'user1': [('#cat #dog fight',1,'1',1,1), \
    ('yolo',1,'1',1,1)], 'user2': [('#cat',1,'1',1,1)]}, '#dog')
    'user1'
    
    >>>detect_author({'user1': [('#cat #dog fight',1,'1',1,1), \
    ('yolo',1,'1',1,1)], 'user2': [('#cat',1,'1',1,1)]}, '#cat #dog')
    'unknown'
    
    >>>detect_author({'user1': [('#cat #dog fight',1,'1',1,1), \
    ('yolo',1,'1',1,1)], 'user2': [('#cat',1,'1',1,1)]}, '#cat #yolo')
    'unknown'
    
    >>>detect_author({'user1': [('#cat #dog fight',1,'1',1,1), \
    ('yolo',1,'1',1,1)], 'user2': [('#cat',1,'1',1,1)]}, 'cat')
    'unknown'
    """
    f = user_tags(d)
    tags = extract_hashtags(text)
    authors = []
    done_tags = []
    
    #check which users have ever used each tag in text, they could be the author
    for tag in tags:
        for user in f:
            if tag in f[user] and user not in authors:
                authors.append(user)
                if tag not in done_tags:
                    done_tags.append(tag)
    if len(done_tags) < len(tags) or len(authors) > 1 or len(authors) == 0:
        return 'unknown'
    return authors[0]
    
    
    
def user_tags(d: Dict[str, List[tuple]]) -> Dict[str, List[str]]:
    """returns a dictionary of users paired with all the unique tags they have 
    ever used.
    
    >>>user_tags({'user1': [('#cat',1,'2',3,4), ('#dog #mouse #cat',1,'2',3,4)],\
    'user2': [('a',1,'2',3,4)]})
    {'user1': ['cat', 'dog', 'mouse'], 'user2': []}
    """
    f = {} #dict to be returned
    for user in d: #checks every user
        f[user] = []
        lst1 = []
        for tweet in d[user]: #checks every tweet
            lst1 = extract_hashtags(tweet[TWEET_TEXT_INDEX])
            for tag in lst1: #collects unique tags in the new dict
                if tag not in f[user]:
                    f[user].append(tag)
    return f
                
    
    
    

if __name__ == '__main__':
    pass

    # If you add any function calls for testing, put them here.
    # Make sure they are indented, so they are within the if statement body.
    # That includes all calls on print, open, and doctest.

    # import doctest
    # doctest.testmod()