# episode 1 --three ways to create a set 
s1 = set ("happysummer")
s1  # {'r', 'p', 'a', 'e', 'h', 'u', 's', 'm', 'y'} set特点：元素无次序，不重复
type(s1)
s2 = set(["worldcup","messi","CR7"]) 
s2  #set()中不能有unhashable即changable元素,所有元素必须是hashable即unchangable元素。此处的set()是unhashable,可以修改set()的元素。
Hashable_set = frozenset() # 此处的set()是hashable,不可以修改frozenset()的元素。
s3 = {"Jordan","James","Kobe","Curry",1948}
s3 
type(s2)
type(s3) 
lst = list(s1)
lst
s4 = set (lst)
s4
# episode 2 --methods of set
""" 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 
'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop',
'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update' """
a_set = {} # 此方法在dict和set中都可以使用。【NOTE】python规定：左边的方法建立的是dict类型,不是set。
type(a_set) 
HotTopic_set = {"sex harassment",20180809,"equality","vaccine","ME&TOO"}
Str_set = set("lookahead")
HotTopic_set.add("GaokaoCheat")
Str_set.add("boy")
HotTopic_set
Str_set
HotTopic_set.update(s2)
HotTopic_set
HotTopic_set.pop() # 从set中任意选一个元素,删除并将这个值返回.
HotTopic_set.remove(20180809) # set.remove(obj)中的obj必须是set中的元素,否则就raise a KeyError。
HotTopic_set
HotTopic_set.discard("equality") # 删除equality
HotTopic_set.discard("Law") # 没有law元素discard就do nothing 
HotTopic_set
HotTopic_set.clear() # Remove all elements from this set.
HotTopic_set
# episode 3 --calculation of set 
Dfc_set = set("diffcult")
Dff_set = set("different")
print(Dfc_set,Dff_set)
Dfc_set == Dff_set
Dfc_set != Dff_set
Dfc_set < Dff_set                    # Dfc_set是Dff_set的子集
Dfc_set.issubset(Dff_set)            # Dfc_set是Dff_set的子集
Dfc_set&Dff_set                      # Dfc_set和Dff_set的交集
Pbl = Dfc_set.intersection(Dff_set)  # Dfc_set和Dff_set的交集
Dfc_set and Dff_set                  # {'n', 'd', 'e', 't', 'f', 'i', 'r'} 即Dff_set why?
Dfc_set | Dff_set                    # Dfc_set和Dff_set的并集
Dfc_set.union(Dff_set)               # Dfc_set和Dff_set的并集
Dfc_set - Dff_set                    # Dfc_set相对Dff_set的不同元素
Dfc_set.difference(Dff_set)          # Dfc_set相对Dff_set的不同元素
Dfc_set.symmetric_difference(Dff_set)# Dfc_set和Dff_set的并集  去除  Dfc_set和Dff_set的交集