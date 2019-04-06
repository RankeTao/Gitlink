# !/usr/bin/env python
# -*- coding: utf-8 -*-

nch = "a new chapter"
for i in nch :
    print( i, end='')  # 打印一行
    if i == nch[len(nch)-1] :
        print('\n')

for j in range(len(nch)) :
    print(nch[j], end='')
print('\n')

# 输出1-100之间能被3整除的列表
Even_num = [] 

for n in range(1,100) :
    if n%3 == 0:
        Even_num.append(n)
print(Even_num)

Bsk_dict = {"Saint Antonio":"Spurs", "Los Angeles":["Lakers","Clippers"], "Cleveland":"Cavaliers", "Golden State":"Warriers"} 
# for 不是循环，是一个iterator，用for实现对dict() K-V pair 的遍历，并显示
for i in Bsk_dict:
    print(i,"/",Bsk_dict[i])
for k in Bsk_dict.keys():
    print(k + "." + str(Bsk_dict[k]))
for k in Bsk_dict: 
    print(k, "-->", Bsk_dict[k])
for k, v in Bsk_dict.items() :
    print(k, v)
for v in Bsk_dict.values():
    print(v, end='#')

# 并行迭代
a = range(10, 50, 10)
b = range(2, 10, 1)
c = []
for i in range(len(a) if len(a)<len(b) else len(b)):
    c.append(a[i]+b[i])
print(list(a), list(b))
print(c)
# 使用zip实现并行迭代
zip(a, b) # 输出结果 <zip object at 0x000001FCD471EE88> why?
zlst = zip(a, b)
list(zlst)       # [(10, 2), (20, 3), (30, 4), (40, 5)]
list(zlst)       # [] 
""" 为什么list(zlst)第二次使用的时候输出空？ 
    答案：Unlike in Python 2, the zip function in Python 3 returns an iterator. 
    Iterators can only be exhausted (by something like making a list out of them) once.
    The purpose of this is to save memory by only generating the elements of the iterator
    as you need them, rather than putting it all into memory at once. If you want to reuse
     your zipped object, just create a list out of it as you do in your second example,
      and then duplicate the list.
    https://stackoverflow.com/questions/31683959/the-zip-function-in-python-3 """
list(zip(a, b))  # [(10, 2), (20, 3), (30, 4), (40, 5)]
list(zip(a, b))  # [(10, 2), (20, 3), (30, 4), (40, 5)]
d = []
for x, y in zip(a, b):
    d.append(x+y)
print(d)
result = list(zip(a, b))
print(list(zip(*result))) #[(10, 20, 30, 40), (2, 3, 4, 5)]

# enumerate:同时得到元素索引和元素 pair
week = ["Monday","Tuesday","Wensday","Thursday","Friday","Saturday","Sunday"]
# 用for迭代器得到week的元素索引和元素
week_dct = {}
for i in range(len(week)):
    print(week[i]+' is '+str(i))
    week_dct[i]=week[i]
print(week_dct)
week_dct.clear()
print(week_dct)
# 用build-in function: enumerate 可以快速得到元素索引和元素 pair
for i, day in enumerate(week):
    print(day+' is '+str(i))
    week_dct[str(i)] = day
print(week_dct)
week_dct.items()
list(enumerate(week)) # a list of tuples
list(enumerate(week,start=1))
# 一种enumerate的用法
slf_intro = "my name is taoshuaiyang, welcome to taoshuaiyang's world"
slfIntro_lst = slf_intro.split(" ")
print(slfIntro_lst)
for i, string in enumerate(slfIntro_lst):
    if 'taoshuaiyang' in string:
        slfIntro_lst[i] = 'RankeTao'  # 如何才能只替换掉name的字符，留下's
print(slfIntro_lst) # 如何再次拼接替换之后的字符list 
" ".join(slfIntro_lst)
# 快速生成指定数列的方法
squares = [x**2 for x in range(1,10)]
squares
