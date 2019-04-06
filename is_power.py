# !/usr/bin/env python
# -*- coding: utf-8 -*-

def is_power(a, b):
    if a%b != 0:
        return f"a is not the power of b"
    elif a / b == 1:
        return True
    else:
        return is_power(a/b, b)

is_power(16, 2)
