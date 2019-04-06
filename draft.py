# !/usr/bin/env python
# -*- coding: utf-8 -*-

# import turtle
# bob = turtle.Turtle()
# bob.pd()
# def draw(t , length , n ) :
#     if n == 0:
#         return
#     angle = 50
#     t.fd(length * n)
#     t.lt(angle)
#     draw(t, length, n-1)
#     t.rt(2*angle )
#     draw(t, length, n-1)
#     t.lt( angle )
#     t.bk(length * n)

# draw(bob, 5, 10)

def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

hi_adam = return_greeting("Adam")
import functools

from __future__ import print_function, division

import time


def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


def make_word_list2():
    """Reads lines from a file and builds a list using list +."""
    t = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        t = t + [word]
    return t


start_time = time.time()
t = make_word_list1()
elapsed_time = time.time() - start_time

print(len(t))
print(t[:10])
print(elapsed_time, 'seconds')

start_time = time.time()
tt = make_word_list2()
elapsed_time = time.time() - start_time

print(len(tt))
print(tt[:10])
print(elapsed_time, 'seconds')

ord(c, /) #'Return the Unicode code point for a one-character string.'
ord(a)