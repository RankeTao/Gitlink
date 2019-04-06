# !/usr/bin/env python
# -*- coding: utf-8 -*-
def fibs(n):
    """
    This is a Fibonacci sequence function. 
    """
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result
if __name__ == "__main__":
    lst = fibs(10)
    print(fibs)

# 至少在python中，递归要慎重使用。在一般情况下，递归是能够被迭代或者循环替代的，而且后者的效率常常比递归要高。
#对使用递归要考虑的周密一下，不小心就永远运行下去了。
def fib(n):
    """
    This is a Fibonacci by recursion. 
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

if __name__ == "__main__":
    f = fib(10)
    print (f)