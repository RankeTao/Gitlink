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