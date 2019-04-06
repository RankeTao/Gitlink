# !/usr/bin/env python
# -*- coding: utf-8 -*-

import turtle
bob = turtle.Turtle()
def polygon(t, length, n): #定义一个画边长为length的n边形的函数
    t.pd()
    for i in range(n):
        t.fd(length)
        t.lt(360.0/n)

import math # 按照惯例应放在开始位置

def circle(t, r):      # 利用polygon函数划近似圆,离散微积分的思想
    circumfence = 2 * math.pi * r
    n = int(circumfence/3)+1 # 每条线段大概是3，这样圆看上去比较逼真，又不失效率
    length = circumfence / n
    polygon(t, length, n)

print(circle(bob, 150))

def arc(t, r, angle):
    circumfence = 2 * math.pi * r * angle /360
    n = int(circumfence/3)+1   # 每条线段大概是3，这样圆看上去比较逼真，又不失效率
    length = circumfence /n
    for i in range(n):
        t.fd(length)
        t.lt(angle/n)

print(arc(bob, 75, 300))
# refractoring 重构：重新整理一个程序以改进函数接口和促进代码复用的过程
def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length/3)+1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length,step_angle)

def circle(t, r):
    arc(t, r, 360)

print(circle(bob, 60))