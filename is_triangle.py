# !/usr/bin/env python
# -*- coding: utf-8 -*-

def is_triangle(a, b, c):
    """
    Judge a b c whether is a triangle
    """
    if a+b < c or a + c < b or b + c < a:
        print("is_trangle: NO")
    else: print("is_trangle: YES")

def Jugde():
    a_stick = int(input("please input an interger a: "))
    b_stick = int(input("please input an interger b: "))
    c_stick = int(input("please input an interger c: "))
    is_triangle(a_stick, b_stick, c_stick)

Jugde()