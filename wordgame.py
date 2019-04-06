# !/usr/bin/env python
# -*- coding: utf-8 -*-

fin = open("words.txt")
fin.readline() # 输出'aa\n'
line = fin.readline()
word = line.strip() # 去除换行符，留下文字
print(word) # 'aah'
fin.close()
#打印长度超过20个字符的单词（不包括空格）
fin = open("words.txt")
word_list = fin.readlines()
for line in word_list:
    word = line.strip()
    if len(word) > 20:
        print(word)
fin.close()
# 写一个函数：如果单词中不包含字母'e'，返回True
def has_no_e(word):
    if 'e' not in word:
        return True
has_no_e('happy')
    #answer
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
#打印输出没有字母'e'的单词，并所占计算比例
fin = open("words.txt")
word_list = fin.readlines()
counter = 0
num_tt = 0
for line in word_list:
    word = line.strip()
    num_tt +=1
    if 'e' not in word:
        counter +=1
        print(word)
percent = counter/num_tt
print("'the percent of words without letter 'e' is {}% ".format(100*percent))
fin.close()
#编写函数：如果单词中不包含任意被禁止的字符，返回true
def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden:
            return False
    return True
#编写函数：如果单词只包括此字符串中的字符，则返回True。
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
#如果单词中的字符以字符表的顺序出现(允许重复字符)，则返回True
# 1,使用for 循环
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
    return True
# 2,使用递归
def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
# 3,while循环
def is_abecedarian(word):
    i = 0
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i += 1
    return True
#判断是否是回文词
def is_palindrome(word):
    i = 0
    j = len(word)-1

    while i < j:
        if word[i] != word[j]:
            return False
        i += 1 
        j -= 1
    return True
# 找出一个包含三个连续双字符的单词。
def is_triple_double(word):
    """Tests if a word contains three consecutive double letters.
    
    word: string

    returns: bool
    """
    i = 0
    count = 0
    while i < len(word)-1:
       if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False


def find_triple_double():
    """Reads a word list and prints words with triple double letters."""
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')
# ex9.8
def has_palindrome(i, start, length):
    """Checks if the string representation of i has a palindrome.

    i: integer
    start: where in the string to start
    length: length of the palindrome to check for
    """
    s = str(i)[start:start+length]
    return s[::-1] == s

    
def check(i):
    """Checks if the integer (i) has the desired properties.

    i: int
    """
    return (has_palindrome(i, 2, 4) and
            has_palindrome(i+1, 1, 5) and
            has_palindrome(i+2, 1, 4) and
            has_palindrome(i+3, 0, 6))


def check_all():
    """Enumerate the six-digit numbers and print any winners.
    """
    i = 100000
    while i <= 999996:
        if check(i):
            print(i)
        i = i + 1


print('The following are the possible odometer readings:')
check_all()
print()
#ex9.9
def str_fill(i, n):
    """Returns i as a string with at least n digits.

    i: int
    n: int length

    returns: string
    """
    return str(i).zfill(n)


def are_reversed(i, j):
    """Checks if i and j are the reverse of each other.

    i: int
    j: int

    returns:bool
    """
    return str_fill(i, 2) == str_fill(j, 2)[::-1]


def num_instances(diff, flag=False):
    """Counts the number of palindromic ages.

    Returns the number of times the mother and daughter have
    palindromic ages in their lives, given the difference in age.

    diff: int difference in ages
    flag: bool, if True, prints the details
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff

        # assuming that mother and daughter don't have the same birthday,
        # they have two chances per year to have palindromic ages.
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """Finds age differences that satisfy the problem.

    Enumerates the possible differences in age between mother
    and daughter, and for each difference, counts the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1

print('diff  #instances')
check_diffs()

print()
print('daughter  mother')
num_instances(18, True)
