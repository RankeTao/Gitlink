# !/usr/bin/env python
# -*- coding: utf-8 -*-

def recurse(n, s):
    """
    return the result of n(n+1)/2 + s 
    """
    if n == 0:
        print(s)
    else: recurse(n-1,n+s)

recurse(4, 4) # 6
recurse(-1,0) # RecursionError: maximum recursion depth exceeded
