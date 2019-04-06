# episode 1 --初识dict
part = ["prism","diffuser","LGP","LB","reflector"]
num = ["44-8011223","44-8021368","44-8031935","44-951183","44-8031479"]
print ("{} : {}".format(part[2],num[2]))
part_num = {"prism":"44-8011223","diffuser":"44-8021368","LGP":"44-8031935","LB":"44-951183","reflector":"44-8031479"}
part_num['B/C'] = '44-8051899' #向dict中增加‘key-value pair’
part_num
BLUDict = {}
id(BLUDict)
BLUDict["M/F"] = "44-8061135"
BLUDict
id(BLUDict) # dict可以原址修改，说明dict是可以改变的
# episode 2 --利用tuple创建不可变dict
# 第一步创建tuple
TPL_partNO = (["prism","44-8011223"],["diffuser","44-8021368"],["LGP","44-8031935"],["LB","44-951183"],["reflector","44-8031479"])
# 第二步创建dict
CONS_partNO = dict(TPL_partNO)
CONS_partNO
# episode 3 --使用fromkeys创建dict
Dct_partNO = {}.fromkeys(("prism","diffuser"),"44-8011223") # 在字典中的“key”，必须是不可变的数据类型；“value”可以是任意数据类型。
Dct_partNO
Dct_partNO["prism"]  # 通过key获取value
""" 
1、len(d)，返回字典(d)中的键值对的数量
2、d[key]，返回字典(d)中的键(key)的值
3、d[key]=value，将值(value)赋给字典(d)中的键(key)
4、del d[key]，删除字典(d)的键(key)项（将该键值对删除）
5、key in d，检查字典(d)中是否含有键为key的项
字典问题是设计一种能够具备关联数组特性的数据结构，这种数据结构包含以下几种常见的操作：
1.向关联数组添加配对 2.从关联数组内删除配对 3.修改关联数组内的配对 4.根据已知的键寻找配对
"""
# episode 3 --methods of dict
# copy()方法，深入理解python内的copy机制
a = 8 
b = a
print(b) 
id(a)  # 1896836384
id(b)  # 1896836384 对象有类型，变量无类型,并没有两个8，只是一个8 用了两个标签a,b表示，这种copy是pseudo-copy
PseudoCopy = part_num
Cpy_partNO = part_num.copy() 
id(part_num)     # 2421259065960  
id(PseudoCopy)   # 2421259065960 
id(Cpy_partNO)   # 2421259066104  地址与part_num 不同说明在内存中另外开辟了储存空间
# shallow copy demonstration
part_num2 = {"prism":"44-8011223","LB":["44-8021368","44-8031935","44-951183"],"reflector":"44-8031479"} 
Shallow_copy = part_num2.copy()
part_num2["LB"].remove("44-8031935")
part_num2
Shallow_copy  # 只删除了part_num2中key对应的一个value，而Shallow_copy中对应的key的那个value也被删除啦
id(part_num2["LB"])     # 2421290713736
id(Shallow_copy["LB"])  # 2421290713736  这里说明了copy的两个dict中对应key都被删除了同一value的原因，两个在一个内存中存储
Shallow_copy["prism"] = "44-0101010"
part_num2         # {'prism': '44-8011223', 'LB': ['44-8021368', '44-951183'], 'reflector': '44-8031479'}
Shallow_copy      # {'prism': '44-0101010', 'LB': ['44-8021368', '44-951183'], 'reflector': '44-8031479'}
id(part_num2)     # 2725195565744
id(Shallow_copy)  # 2725195565816  python存储的特点是只存储基本类型的数据类型，比如int,str，对于不是基础类型的数据，采用引用方式
# deep copy demonstration
import copy 

part_num2         # {'prism': '44-8011223', 'LB': ['44-8021368', '44-951183'], 'reflector': '44-8031479'}
Deep_copy = copy.deepcopy(part_num2) 
Deep_copy["LB"].remove("44-8021368") 
part_num2["LB"].append("44-1000100")
Deep_copy
part_num2
id(part_num2["LB"])  # 2360964846856
id(Deep_copy["LB"])  # 2360964864712   deep copy 之后重新分配内存而不是引用

# episode 4 --clear 与 del 的区别
part_num2.clear() 
part_num2         # part_num2变成一个空dict,即part_num2 = {} ,此方法仍然可以使用
del part_num2
part_num2         # del将part_num2直接从内存中删除，再使用它则提示NameError: name 'part_num2' is not defined 

# episode 5 --get ,setdefault, items,iteritems, keys,iterkeys, values,itervalues
part_num.get("LB")
part_num.setdefault("PCB")
ITM_partNO = part_num.items()
KY_partNO = part_num.keys() 
Vlu_partNO = part_num.values()
ITM_partNO
KY_partNO
Vlu_partNO
""" 在Python2.x中，items( )用于 返回一个字典的拷贝列表【Returns a copy of the list of all items (key/value pairs) in D】，
占额外的内存。iteritems() 用于返回本身字典列表操作后的迭代【Returns an iterator on all items(key/value pairs) in D】，
不占用额外的内存。  
Python 3.x 里面，iteritems() 和 viewitems() 这两个方法都已经废除了，而 items() 得到的结果是和 2.x 里面 viewitems() 一致的。
在3.x 里 用 items()替换iteritems() ，可以用于 for 来循环遍历。"""
# ITM_iter = part_num.iteritems() 
