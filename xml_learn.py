"""python提供了多种模块来处理
1、xml.dom.* 模块：Document Object Model。适合用于处理 DOM API。它能够将xml数据在内存中解析成一个树，然后通过对树的操作来操作xml。
但是，这种方式由于将xml数据映射到内存中的树，导致比较慢，且消耗更多内存。
2、xml.sax.* 模块：simple API for XML。由于SAX以流式读取xml文件，从而速度较快，切少占用内存，但是操作上稍复杂，需要用户实现回调函数。
3、xml.parser.expat：是一个直接的，低级一点的基于 C 的 expat 的语法分析器。 
expat接口基于事件反馈，有点像 SAX 但又不太像，因为它的接口并不是完全规范于 expat 库的。
4、xml.etree.ElementTree (以下简称 ET)：元素树。它提供了轻量级的python式的API，相对于DOM，ET快了很多 ，
而且有很多令人愉悦的API可以使用；相对于SAX，ET也有ET.iterparse提供了 “在空中” 的处理方式，
没有必要加载整个文档到内存，节省内存。ET的性能的平均值和SAX差不多，但是API的效率更高一点而且使用起来很方便。"""

import xml.etree.ElementTree as ET 
tree = ET.parse("bookstore.xml") # 建立起xml解析树,然后可以通过根节点向下开始读取各个元素（element对象）。
tree
root = tree.getroot() # 获得根
root.tag
root.attrib

for child in root:
    print(child.tag, child.attrib)

root[0].tag 
root[0].attrib
root[0].text 

root[0][0].tag
root[0][0].attrib
root[0][0].text 

# 对于ElementTree对象，有一个iter方法可以对指定名称的子节点进行深度优先遍历。
for ele in tree.iter(tag="book"):
    print(ele.tag, ele.attrib)
for ele in tree.iter(tag="title"):
    print(ele.tag, ele.attrib, ele.text)

# 如果不指定tag名称，则将所有元素遍历一遍
for ele in tree.iter():
    print(ele.tag, ele.attrib, ele.text ) 
# 还可以通过路径，搜索到指定的元素，读取其内容。这就是xpath。
for ele in tree.iterfind("book/title"):
    print(ele.text)
# 利用findall()方法，也可以实现查找功能
for ele in tree.findall("book"):
    title = ele.find("title").text
    price = ele.find("price").text 
    author = ele.find("author").text
    lang = ele.find("title").attrib
    print(author, title, price, lang, sep="/")

# edit xml
root[1].tag 
del root[1] # 源文件还没有变化，因为至此的修改动作，只是停留在内存中，还没有将修改结果输出到文件。不要忘记，我们是在内存中建立的ElementTree对象。
for ele in root:
    print(ele.tag)
# 将修改写入xml文件中
import os 
outpath = os.getcwd()
file = outpath + "/bookstore.xml" # 拼接文件路径
tree.write(file) # 此时bookstore.xml文件中只有两个book节点
# 修改价格、增加属性标记，并写入xml文件
for price in tree.iter("price"):
    print(price.text)
for price in tree.iter("price"):
    new_price = float(price.text) + 7
    price.text = str(new_price)
    price.set("update", "up")
tree.write(file)
#上面用del来删除某个元素，其实，在编程中，这个用的不多，更喜欢用remove()方法。
for book in tree.findall("book"):
    price = book.find("price").text 
    if float(price) > 40:
        root.remove(book)
tree.write(file) # 此时bookstore.xml文件中只有一个book节点

ET.SubElement(root, "book") # 在root里面添加book节点
for ele in root:
    print(ele.tag)
b2 = root[1] # 得到新增的book节点
b2.text = "python" # 添加内容
tree.write(file)
"""常用属性和方法总结
ET里面的属性和方法不少，这里列出常用的，供使用中备查。
Element对象
    常用属性：
    tag：string，元素数据种类
    text：string，元素的内容
    attrib：dictionary，元素的属性字典
    tail：string，元素的尾形
    针对属性的操作
    clear()：清空元素的后代、属性、text和tail也设置为None
    get(key, default=None)：获取key对应的属性值，如该属性不存在则返回default值
    items()：根据属性字典返回一个列表，列表元素为(key, value）
    keys()：返回包含所有元素属性键的列表
    set(key, value)：设置新的属性键与值
    针对后代的操作
    append(subelement)：添加直系子元素
    extend(subelements)：增加一串元素对象作为子元素
    find(match)：寻找第一个匹配子元素，匹配对象可以为tag或path
    findall(match)：寻找所有匹配子元素，匹配对象可以为tag或path
    findtext(match)：寻找第一个匹配子元素，返回其text值。匹配对象可以为tag或path
    insert(index, element)：在指定位置插入子元素
    iter(tag=None)：生成遍历当前元素所有后代或者给定tag的后代的迭代器
    iterfind(match)：根据tag或path查找所有的后代
    itertext()：遍历所有后代并返回text值
    remove(subelement)：删除子元素
ElementTree对象
    find(match)
    findall(match)
    findtext(match, default=None)
    getroot()：获取根节点.
    iter(tag=None)
    iterfind(match)
    parse(source, parser=None)：装载xml对象，source可以为文件名或文件类型对象.
    write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None,method="xml")"""