# !/usr/bin/env python
# -*- coding: utf-8 -*-

#将原来对输入数字范围判断是否在1-100以内，修改为判断新输入的数字是否在新生成的lst_input内，如果不在输出提示！

import random                  # 导入随机模组

Xnum = random.randint(1, 101)  # 系统生成一个1-100之间的随机数字
guess = 0                      # 为变量guess定义一个初始值
Lst_input = list(range(1,101)) # 将1-100生成一个list
#print(Lst_input)              # 调试时检验输出
#print(Xnum)                   # 调试时显示系统生成的随机数
while True:                    # 开始while循环
    # 输入一个1-100的整数
    num_input = input("please enter an integer number between %d to %d: " % (Lst_input[0],Lst_input[-1]))
    guess +=1   # 计算所有输入次数，包括输错的次数
    # 【IMPORTANT】任何用户输入的内容都是不可靠的。所以要判读用户输入了什么，并给予相应的提示语句。
    # 判断输入是否是数字，如果不是，输出提示"please input an interger."
    if not num_input.isdigit():
        print("please input an interger.")
    # 判断输入是否在重新生成的Lst_input内，如果不在，输出相应的提示."
    elif int(num_input) not in Lst_input:
        print("The integer number is out of range. It should be %d to %d." % (Lst_input[0],Lst_input[-1]))
    else:
        # 前两步判断最新输入的是数字且在新生成的Lst_input内，将用户输入的数字添加进List_input里面，并从小到大排序 
        Lst_input.append(int(num_input))
        Lst_srt = sorted(Lst_input)
        #print(Lst_srt)  #调试时检验输出是否符合预期
        x = Lst_input.index(int(num_input))  # 检索用户输入数字排序之后在list_srt中的位置，在此将序列分成上下两个区间
        #print(x)   # 调试时检验输出
        #guess +=1   # 计算合法输入(有效输入）的次数
        # 输入数字与系统产生数字相等，则输出成功提示，退出循环
        if int(num_input) == Xnum:
            print("You've got it.Congratulations! Lucky you. It only takes %d times." % guess)
            break
        # 如果系统生成的随机数在上半区间，并提示用户输入上半区间内的整数，并将上班区间赋值给list_input
        elif Xnum in Lst_srt[:x]:
            print("It is closer to the Random Number! Please Try again!")
            Lst_input = Lst_srt[:x]
        # 如果系统生成的随机数在下半区间，并提示用户输入下半区间内的整数，并将上班区间赋值给list_input
        else: 
            print("It is closer to the Random Number! Please Try again!")
            Lst_input = Lst_srt[x:]
        #print(Lst_input) # 调试时检验输出