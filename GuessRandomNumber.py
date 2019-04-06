# !/usr/bin/env python
# -*- coding: utf-8 -*-
import random

Xnum = random.randint(1, 101)
guess = 0
Lst_input = []

while  True:

    num_input = input("please enter an integer number between 1 and 100: ")
   
    if not num_input.isdigit():
        print("please input an interger.")
    elif int(num_input)<0 or int(num_input)>100:
        print("The number should be 1 to 100")
    else:
        Lst_input.append(num_input)
        guess +=1 
        print(Lst_input)

        if int(num_input) == Xnum:
            print("OK, Lucky you.It is only %d times, then you successed." % guess)
        elif int(num_input) > Xnum:
            if guess == 1: print("your number is bigger.It should be 1 to %d." % int(Lst_input[-1]))
            elif guess == 2: print("your number is bigger.It should be 1 to %d." % int(Lst_input[0]))
            elif Lst_input[-1] > Lst_input[-2]: print("Please input a smaller number than last number between 1 to %d." % int(Lst_input[len(Lst_input)-guess]))
            else: print("your number is bigger. It should be 1 to %d." % int(Lst_input[-1]))
        elif int(num_input) < Xnum:
            if guess == 1: print("your number is more less.It should be %d to 100." % int(Lst_input[-1]))
            elif guess == 2: print("your number is more less.It should be %d to 100." % int(Lst_input[0]))
            elif Lst_input[-1] < Lst_input[-2]: print("please input a bigger number than last number between %d to 100." % int(Lst_input[len(Lst_input)-guess]))
            else: print("your number is more less. It should be %d to 100" % int(Lst_input[-1]))
        else:
            print("There is something bad, It will not work")
    print('\n')