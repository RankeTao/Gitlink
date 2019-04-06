"""
循环（loop），指的是在满足条件的情况下，重复执行同一段代码。比如，while语句。
迭代（iterate），指的是按照某种顺序逐个访问列表中的每一项。比如，for语句。
递归（recursion），指的是一个函数不断调用自身的行为。比如，以编程方式输出著名的斐波纳契数列。
遍历（traversal），指的是按照一定的规则访问树形结构中的每个节点，而且每个节点都只访问一次。
记得搜索这几个术语之间的对比 """

lst = list("Hamlet")
lst
lst_iter = iter(lst)
lst_iter.__next__()
lst_iter.__next__()
lst_iter.__next__()
lst_iter.__next__()
lst_iter.__next__()
lst_iter.__next__()
lst_iter.__next__()

lst_iter = iter(lst)
while True:
    print(lst_iter.__next__())

# 文件迭代
f = open("Youth.txt")
for line in f:
    print(line, end = "")
#f.close()

f2 = open("newfile.txt") 
f2.__next__()         # 不需要用iter()转换就可以直接读取每行的内容。这说明文件是天然的可迭代对象。
f2.__next__()
f2.__next__()
f2.close()

[line for line in open("Youth.txt")]
list[open("newfile.txt")]
tuple(open("newfile.txt"))
"@".join(open("newfile.txt"))
