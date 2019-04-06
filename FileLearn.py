# episode 1 --打开文件
f = open("C:\\Users\\iweut\\PythonTest\\testGit.txt") # 如在当前文件夹内也可以这样打开文件open("testGit.txt")
for line in f:
    print(line, end = "")
"""前一次已经读取了文件内容，并且到了文件的末尾了。再重复操作，就是从末尾开始继续读了。当然显示不了什么东西，
但是python并不认为这是错误，因为后面就会讲到，或许在这次读取之前，已经又向文件中追加内容了。
那么，如果要再次读取怎么办？就从新来一边好了。这就好比有一个指针在指着文件中的每一行，每读完一行，指针向移动一行。
直到指针指向了文件的最末尾。当然，也有办法把指针移动到任何位置。"""
for line2 in f:     
    print(line2)   # 没有输出,如果两次都用open()的话，则可以输出
# episode 2 --创建文件
""" r 模式 以读方式打开文件，可读取文件信息
    w 模式 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件
    a 模式 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
            也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 """
nf = open("newfile.txt","w")   #打开一个文件，W模式
nf.write("This a new file created just now") # 写入文件的内容
nf.close()  #必须使用close()关闭文件，否则输出结果则是32(写入字符的个数) 为什么？
nf2 = open("newfile.txt")
for line3 in nf2:
    print(line3, end = "")

nf3 = open("testGit.txt", "a")
nf3.write("Learn more about how to deploy git. please visit:www.")
nf3.close()
nf4 = open("testGit.txt")
for line4 in nf4:
    print(line4, end="")
# with 语句 可以不写close() ,能够安全的关闭文件，这种做法更python一点
with open("newfile.txt", "a") as nf5:
    nf5.write("\nThis a showcase about how to use 'with...as...' method")
with open("newfile.txt") as nf5:
    nf5.read()
# episode 3 --
import os   # 导入python的os 模块
import time # 导入python的time模块

file_stat = os.stat("testGit.txt") # 查看这个文件的状态
file_stat                          # 显示文件状态
file_stat.st_ctime                 # 文件创建时间
time.localtime(file_stat.st_ctime) # 使用time模块输出常规格式

f1 = open("Youth.txt")
content = f1.read()
content
f1.close() #打开一个文件之后，要记得及时close，否则会一直驻留在内存中，不仅浪费空间，还会增加数据的安全风险
print(content)

# 用readline读取
f1 = open("Youth.txt") #前面关闭了文件，需再次打开
f1.readline() 
f1.readline()
f1.readline() # 每次操作向下读取一行，指针向下移动一行，可以循环迭代，完成对全文的读取
f1.close()

# !/usr/bin/env python
# -*- coding: utf-8 -*-

f3 = open("Youth.txt")

while True:
    Per_line = f3.readline()  # 读取一行之后赋值给Per_line变量
    if not Per_line:          # Per_line如果是空，if判断条件为True，表示文件读取完毕，break跳出while循环
        break
    print(Per_line, end="")   # 因原文有换行，所以在打印的时候用end = ""去掉print的默认换行操作

f3.close()                    # 别忘了顺手关闭文件

#用readlines读取文件

f4 = open("Youth.txt")
content2 = f4.readlines()  # readlines将每一行作为一个元素，生成一个string list,所以content2 是一个字符串列表
content2

for everyLine in content2:
    print(everyLine, end="")

# read a big file:
# 方法一：如果一个文件很大，则不宜使用read()、readlines()一次性的将全部内容读取到内存中，可以使用while循环和readline()来完成。
# 方法二：fileinput模块的input命令和for循环搭配使用

import fileinput

for eachLine in fileinput.input("Youth.txt"):
    print(eachLine, end="") 

# seek() 以字节为单位移动指针；tell() 显示此时指针所在的位置
f5 = open("Youth.txt")
f5.readline()
f5.readline()
f5.tell()
f5.seek(0)
f5.readline()
f5.seek(3)
f5.readline()
f5.readline()
f5.tell()
f5.readline()
f5.tell()
f5.close()

""" seek(...) seek(offset[, whence]) -> None. Move to new file position.
Argument offset is a byte count. Optional argument whence defaults to 0 (offset from start of file, offset should be >= 0); 
other values are 1 (move relative to current position, positive or negative), 
and 2 (move relative to end of file, usually negative, although many platforms allow seeking beyond the end of a file).
If the file is opened in text mode, only offsets returned by tell() are legal. 
Use of other offsets causes undefined behavior. 
Note that not all file objects are seekable.
seek()函数的参数whence:
默认值是0，表示从文件开头开始计算指针偏移的量（简称偏移量）。这是offset必须是大于等于0的整数。
是1时，表示从当前位置开始计算偏移量。offset如果是负数，表示从当前位置向前移动，整数表示向后移动。
是2时，表示相对文件末尾移动。"""