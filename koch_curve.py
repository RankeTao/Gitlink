# !/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle

bob = turtle.Turtle()

def KochCurve(t, length):
    if length < 5:
        t.fd(length)
        return
    t.pd()
    step = length/3
    KochCurve(t, step)
    t.lt(60)
    KochCurve(t, step)
    t.rt(120)
    KochCurve(t, step)
    t.lt(60)
    KochCurve(t, step)

def SnowFlake(t, length, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(n):
        KochCurve(t, length)
        angle = 360.0/n
        t.rt(angle)

SnowFlake(bob, 100, 6)