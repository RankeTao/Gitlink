#episode 1
print("abcd")
a = 5
b = 6
print( a+b )
#episode 2
lang = "python"  #str类型
lang.index("t")
lang[-1:-3]
lang[-3:-1]  #左边的数字应小于右边的数字，若不是，则返回空''
lst = ['wo','ni','456']  #list类型，与str都属于序列
lst.index('wo')
lst[-2:-1]
#episode 3 --reverse颠倒顺序
alst = ['1',2,'3','4',5,'6']
alst[::-1]
alst
lang[::-1]  #这里的反转，不是在“原地”把原来的值倒过来，而是新生成了一个值，那个值跟原来的值相比，是倒过来了。
list(reversed(alst))  #python内置的reversed函数
list(reversed(lang))  #这里的反转输出在表示形式上与lang[::-1]有点区别，需要注意
#episode 4 --基本操作
max(alst) #max() min() cmp()都只能比较相同类型的元素，如果是int则比较大小，如果不是，按照字符在ASCII编码中所对应的数字进行比较的
# cmp(lst,alst) #python3.6.5找不到此函数
lst+alst
lst*3
2 in alst
'2' in alst
#episode 5 --add element
ln = [1,"a","30","good"]
lm = ["I","like","it"]
len(ln)
ln[len(ln):] = [100]
ln
ln.append("morning") #list.append 添加的内容（不管是单个元素，还是一个list类型）都将作为一个元素到list
ln
ln.extend(lm)  #此操作与ln+lm效果相同，lista.extend(listb)添加一个listb到另一个lista
ln
la = "Hamlet"
ln.extend(la) #extend扩展的对象一定是list类型，la是一个str类型，所有python会先将str转换成list类型，再扩展到list
ln
a = 3
hasattr(a,'__iter__')   #用内建函数hasattr()判断一个字符串是否是可迭代的
hasattr(la,'__iter__')  #hasattr()的判断本质就是看那个类型中是否有__iter__函数。
hasattr(ln,'__iter__')
id(ln)  #在内存的位置
ln.extend(la)
id(ln)
#扩展之后在内存中的位置并没有改变
#【IMPORTANT】list的重要特征：列表是可以修改的。这种修改，不是复制一个新的，而是在原地进行修改，
# 原地修改，没有返回值，就不能赋值给某个变量。
ln.insert(2,"nice")
ln
ln.insert(100,"to") # 如果遇到那个i已经超过了最大索引值，会自动将所要插入的元素放到列表的尾部，即追加。
ln
ln.remove("good")
ln
ln.pop(5)
ln.pop()
numlst = [1,2.3,8.6,9,42]
numlst.sort()
numlst
numlst.reverse()
numlst
numlst.sort(reverse=True)
numlst
# list和str的最大区别是：list是可以改变的，str不可变。
numlst[2] = "Peking"
numlst
myhome = "l u\toh\ne" # create a 'str' object
# myhome[3] = "Y" # TypeError: 'str' object does not support item assignment
myhome
myhome.split()
# episode 6 --tuple
tpl =(1,"wo", ("world","peace",3,"now"))
lst2 = [1,"wo", ("world","peace",3,"now")]
type(tpl)
type(lst2)
# 所有在list中可以修改list的方法，在tuple中，都失效。
"""一般认为,tuple有这类特点,并且也是它使用的情景:
1、Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
2、如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，
说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
3、Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
4、Tuples 可以用在字符串格式化中。
5、通常不对list使用别名alias，因为list是可变的，可以对str使用alias，str不可变"""
# 【IMPORTANT】 对象有类型，变量无类型

#ex10.1
total = 0
def nested_sum(t):
    global total
    for element in t:
        print(element)
        if isinstance(element, list):
            return nested_sum(element)
        else:
            total += element
 
    return total

t = [[1, 2, 3, 8], [3], [4, 5, 6]]
nested_sum(t) # for循环结束，只计算了一个第一个嵌套list
type(t[1][0])
isinstance(t[1], list)
