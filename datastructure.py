# !/usr/bin/env python
# -*- coding: utf-8 -*-

#ex13.1
import string

punc_str = string.whitespace + string.punctuation + '“”—'
whitespace_str = ''
for i in range(len(punc_str)):
    whitespace_str += ' '
table = str.maketrans(punc_str, whitespace_str) # 生产一个将标点符号对应空格的table，punc_str和whitespace_str的长度相等

def make_word_list(filename):
    fin = open(filename, 'r', encoding= 'utf-8')
    words_list = []
    for line in fin:
        words_per_line = line.translate(table).split() 
        for eword in words_per_line:
            word = eword.strip().lower()
            words_list.append(word)
    return words_list

make_word_list("frankenstein.txt")
#13.2

def context(filename):
    """Extract content from file by delete beginning and end of file.
    Returns: a list of every line of text.
    """
    fin = open(filename, 'r', encoding= 'utf-8')
    lines = fin.readlines()
    line_range = []
    for line in lines:
        if line.startswith('***'):
            line_range.append(lines.index(line))
    context = lines[line_range[0]+1:line_range[1]]
    return context


total = 0
def make_word_dict(text):
    """Make a map from word to number of times they appear in text.
    text: list of every line of text
    Returns: map from word to frequency
    """
    words_dict = {}
    global total 
    for per_line in text:
        words = per_line.translate(table).split()
        for eword in words:
            word = eword.strip().lower()
            if word.isalpha :
                total += 1
                words_dict[word] = words_dict.get(word, 0) + 1
            else:
                pass
    return words_dict

content = context('frankenstein.txt')
print(content[0:10])
word_statis = make_word_dict(content)
len(word_statis)
print(total)

content = context('prideandprejudice.txt')
print(content[0:10])
word_statis = make_word_dict(content)
len(word_statis)
print(total)
#ex13.3

def print_frequent_words(dct):
    """Print top 10 frequently used words.
    dct:  map from word to frequency
    """
    t = []
    for key in dct.keys():
        t.append((dct[key], key))
        t.sort(reverse = True)
    
    for _, word in t[0:10]:
        print(word, _, sep='\t')

print_frequent_words(word_statis)
