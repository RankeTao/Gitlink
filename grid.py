# !/usr/bin/env python
# -*- coding: utf-8 -*-

def gird(m, n):
    """
    draw a m row n column gird with subgrid of 5 row 5 column
    """
    for x in range(m+1): # 一行一行打印
        if x%5 == 0:     # 满足一定条件的行
            for y in range(n+1): # 一列一列循环打印
                if y%5 ==0: # 满足一定条件的列打印特殊符号“+”
                    print('+',end=' ')
                else: print('-',end=' ') # 其余列打印“- ”
        
        elif x%5 != 0: # 不满足一点条件的列
            for y in range(n+1): 
                if y%5 == 0: # 满足条件的列打印“| ”
                    print('|',end=' ')
                else: print('  ', end='') #其余输出2空格匹配空间
        print()
gird(20, 20)