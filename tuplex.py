# !/usr/bin/env python
# -*- coding: utf-8 -*-

#ex12.1
def most_frequent(s):
    """Sorts the letters in s in reverse order of frequency.

    s:string

    Returns: list of letters
    """

    hist = make_histogram(s)

    t = []
    for x, freq in hist.items():
        t.append((freq, x))
    
    t.sort(reverse = True)
    # print(t)
    res = []
    for freq, x in t:
        res.append(x)
    
    return res

def make_histogram(s):
    """Make a map from letters to number of time they appear in s.

    s:string

    Returns: map from letter to frequency
    """
    hist = {}
    for x in s:
        if x is '\n':
            pass
        else:
            hist[x] = hist.get(x, 0) + 1
    return hist

def read_file(filename):
    """Reaturns the contents of a file as a string."""
    return open(filename).read()

if __name__ == '__main__':
    string = read_file("words.txt")
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)
# ex12.2
def make_word_list(filename):
    fin = open(filename)
    word_lst = []
    for word in fin:
        word_lst.append(word.strip().lower())
    return word_lst

wordlst = make_word_list("words.txt")

def anagrams(word_lst):
    """map from word to list of anagrams"""
    words_dict = {}
    for word in word_lst:
        characters = ''.join(sorted(list(word)))
        if characters in words_dict:
            words_dict[characters].append(word)
        else:
            words_dict[characters] = [word]
    return words_dict

wrd_dct = anagrams(wordlst)

def print_anagrams(words_dict):
    """打印包含异位构词数量最多的词汇列表，第二多次之，依次按异位构词数量排列."""
    len_v_k_lst = []
    for v in words_dict.values():
        len_v_k_lst.append((len(v), v))
    len_v_k_lst.sort(reverse = True)
    for i in range(1, 10):
        print(len_v_k_lst[i])

print_anagrams(wrd_dct)

#ex12.3
def word_difference(word1,word2):
    """Computes the number of differneces between two words
    word1, word2: strings
    Returns: integer
    """
    assert len(word1) == len(word2)

    count = 0 
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count +=1
    return count

def metathesis_pairs(words_dict):
    """print all pairs of words that differ byb swapping two letters
    d: map from word to list of anagrams
    """
    for anagrams in words_dict.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_difference(word1, word2) ==2:
                    print(word1, word2)
metathesis_pairs(wrd_dct)

#ex12.4
def sub_words(word):
    """creat a list of words which a character is substracted from a word"""
    sub_words_lst = []
    for i in range(len(word)):
        sub_word = word[:i]+word[i+1:]
        sub_words_lst.append(sub_word)
    return sub_words_lst


def is_subtractable(word, wordlst):
    sub_wordlst = sub_words(word)
    for word in sub_wordlst:
        if word in wordlst:
            if word != 1:
                return is_subtractable(word, sub_wordlst)
            else:
                return True
        else:
            pass
    return False

is_subtractable("spit", wordlst)
#answer

#from __future__ import print_function, division
# 1、必须在文档的开头，2、在开头加上from __future__ import print_function
# 这句之后，即使在python2.X，使用print就得像python3.X那样加括号使用。
###-----------------------------------------------------------###
def make_word_dict():
    """Reads a word list and returns a dictionary"""
    d = dict()
    fin = open("words.txt")
    for line in fin:
        word = line.strip().lower()
        d[word] = None
    #have to add single letter words to the word list;
    #also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d

"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children. It starts
with the empty string."""

memo = {}
memo[''] = ['']

def is_reducible(word, word_dict):
    """If word is reducible, returns a list of its reducible children.
    Also adds an entry to the memo dictionary. 
    A string is reducible if it has at least one chils that is reducible. 
    The empty string is also reducible. 
    word: string
    word_dict: dictionary with words as keys
    """
    # if have already checked this word, return the answer
    if word in memo:
        return memo[word]
    
    # check each of the children and make a list of the reducible ones
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(child)
    #memorize and return the result
    memo[word] = res
    return res

def children(word, word_dict):
    """Returns a list of all words that can be formed by removing one letter.
    word: string
    Returns: list of strings
    """
    res = []
    for i in range(len(word)):
        child = word[:i]+word[i+1:]
        if child in word_dict:
            res.append(child)
    return res 

def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.
    word_dict: dictionary with words as keys
    """
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res

def print_trail(word):
    """Print the sequence of words that reduces this word to the empty string.
    If there is more than one choice, it chooses the first.
    word: string
    """
    if len(word) == 0:
        return
    print(word, end = ' ')
    t = is_reducible(word, word_dict)
    print_trail(t[0])

def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them. 
    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)
    
    #Print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')

word_dict = make_word_dict()
children("strarnger", word_dict)
is_reducible("stranger", word_dict)
all_reducible(word_dict)
print_trail('stranger')
print_longest_words(word_dict)
#if __name__ == '__main__':
