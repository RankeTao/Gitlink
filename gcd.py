# !/usr/bin/env python
# -*- coding: utf-8 -*-

def gcd(a, b):
    if b == 0:
        return a 
    else:
        return gcd(b, a%b)

gcd(99, 63)