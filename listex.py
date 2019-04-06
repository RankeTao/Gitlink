# !/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
import time

def timer(func):
    """
    Print the runtime of the decorated function
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time() # the time just before the func starts running
        value = func(*args, **kwargs)
        end_time = time.time() # the time just before the func starts running
        run_time = end_time - start_time # time intervals
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def read_words_1(file):
    """Read lines from file"""
    fl = open(file)
    word_lst = []
    for line in fl:
        word = line.strip()
        word_lst.append(word)
    fl.close()
    return word_lst

t = read_words_1("words.txt")
print(t[:10])

@timer
def read_words_2(file):
    """Read lines from file"""
    fl = open(file)
    word_lst = []
    for line in fl:
        word = line.strip()
        word_lst = word_lst + [word]
    fl.close()
    return word_lst

#tt = read_words_2("words.txt")
#print(tt[:10])

@timer
def read_words_3(file):
    """Read lines from file"""
    fl = open(file)
    word_lst = []
    for line in fl:
        word = line.strip()
        word_lst += [word]
    fl.close()
    return word_lst

ttt = read_words_3("words.txt")
print(ttt[:10])
#以上三种函数的运算时间read_words_2 >> read_words_1 > read_words_3
######################################################################
# look up some word in word_lst
@timer
def find_word(word_lst, word):
    if word in word_lst:
        return word_lst.index(word)
    else:
        return print("%s is not in" % word)

find_word(t, "happy")

import bisect
@timer
def in_bisect1(sorted_lst, word):
    i = bisect.bisect_left(sorted_lst, word)
    return i
in_bisect1(t, "happy")
# answer
def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string

    returns: True if the word is in the list; False otherwise
    """
    if len(word_list) == 0:
        return False

    i = len(word_list) // 2
    if word_list[i] == word:
        return True

    if word_list[i] > word:
        # search the first half
        return in_bisect(word_list[:i], word)
    else:
        # search the second half
        return in_bisect(word_list[i+1:], word)
####################################################################
@timer
def reverse_pair1(word_lst):
    word_pair = []
    for word in word_lst:
        if word[::-1] in word_lst:
            word_pair.append((word, word[::-1]))
        else:
            pass
    return word_pair[-10:]

reverse_pair1(t)

@timer
def reverse_pair(word_lst):
    word_pair = []
    for word in word_lst:
        if in_bisect(word_lst,word[::-1]):
            word_pair.append((word, word[::-1]))
        else:
            pass
    return word_pair[-10:]

reverse_pair(ttt)

############################################################
#answer
def reverse_pair2(word_list, word):
    """Checks whether a reversed word appears in word_list.

    word_list: list of strings
    word: string
    """
    rev_word = word[::-1]
    return in_bisect(word_list, rev_word)
        

t1 = read_words_1("words.txt")
@timer
def show_word_pair(word_lst):    
    for word in word_lst:
        if reverse_pair2(word_lst, word):
            print(word, word[::-1])

show_word_pair(t1)