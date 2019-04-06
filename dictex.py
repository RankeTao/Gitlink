# !/usr/bin/env python
# -*- coding: utf-8 -*-

def histogam(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
    return d

histogam("everyday")

# 使用get方法简化histogram函数
# 字典类有一个get 方法，接受一个键和一个默认值作为参数。
# 如果字典中存在该键，则返回对应值；否则返回传入的默认值。
def histogam(s):
    d = dict()
    for c in s:
        cnum = d.get(c, 0)
        cnum += 1
        d[c] = cnum
    return d

dct = histogam("everyday")
s_dct = sorted(dct)
s_dct
def print_hist(h):
    for c in h:
        print(c, h[c])

print_hist(dct)

for key in s_dct:
    print(key, dct[key])
#########################################
import random
import functools
import time
# timer decorator
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
# compare the speed of finding str
word_dict = dict()
word_lst = []
fl = open("words.txt")
for line in fl:
    word = line.strip()
    word_dict[word] = random.randint(0, 10000)
    word_lst.append(word)
fl.close()

@timer
def check_str(str):
    """Check str whether in dict or not"""
    if str in word_dict:
        return True
    else:
        return False

@timer
def check_str2(str):
    """Check str whether in list or not"""
    if str in word_lst:
        return True
    else:
        return False
word_dict
check_str("zoo")
check_str2("happy")
#exchange key and value pair
def invert_dict_1(dct):
    inverse = dict()
    for key in dct:
        val = dct[key]
        if val not in dct:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
# 使用dict.setdefault方法
def invert_dict(dct):
    inverse_word_dict = dict()
    for key in dct:
        val = dct[key]
        inverse_word_dict.setdefault(val, key)
    return inverse_word_dict

invert_dict_1(word_dict)
invert_dict(word_dict)
#rewrite has_duplicates function in ex10.7
def has_duplicates(lst):
    lst_to_dict = {}
    for x in lst:
        counter = lst_to_dict.get(x, 0)
        counter += 1
        lst_to_dict[x] = counter
        if counter >= 2:
            return True
    return False

has_duplicates([1, 2, 2])
