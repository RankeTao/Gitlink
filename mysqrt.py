# !/usr/bin/env python
# -*- coding: utf-8 -*-

def mysqrt(a):
    while True:
        x = 5
        print ( x )
        y=(x + a / x ) / 2
        if y == x :
            break
        x = y

mysqrt(4)