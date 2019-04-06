# !/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def mysqrt(a):
    x = 1
    while True:
        y = (x + a / x ) / 2
        if y == x :
            break
        x = y
    return y

mysqrt(2)
