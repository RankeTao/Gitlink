# !/usr/bin/env python
# -*- coding: utf-8 -*-

# urllib模块的学习：快速使用Urllib爬取网页

import urllib.request

file_data = urllib.request.urlopen("https://www.python.org/")
handle_data  = open("./0818.html", 'wb')
handle_data.write(file_data.read())
handle_data.close()

file_data.info()
file_data.getcode()
file_data.geturl()
"""一般来说，URL标准中只会允许一部分ASCII字符比如数字、字母、部分符号等，而其他的一些字符，比如汉字等，是不符合URL标准的。此时，我们需要编码。 
如果要进行编码，我们可以使用urllib.request.quote()进行，比如，我们如果要对百度网址进行编码："""
urllib.request.quote('http://www.baidu.com') # 编码结果：'http%3A//www.baidu.com'
urllib.request.unquote('http%3A//www.baidu.com') # 解码结果：'http://www.baidu.com'

"""对url编码、解码
url对其中的字符有严格要求，不许可某些特殊字符，这就要对url进行编码和解码了。这个在进行web开发的时候特别要注意。urllib模块提供这种功能。
quote(string[, safe])：     对字符串进行编码。参数safe指定了不需要编码的字符
urllib.unquote(string) ：   对字符串进行解码
quote_plus(string [ , safe ] ) ：   与urllib.quote类似，但这个方法用'+'来替换空格' '，而quote用'%20'来代替空格
unquote_plus(string ) ：    对字符串进行解码；
urllib.urlencode(query[, doseq])：  将dict或者包含两个元素的元组列表转换成url参数。例如{'name': 'laoqi', 'age': 40}将被转换为"name=laoqi&age=40"
pathname2url(path)：    将本地路径转换成url路径
url2pathname(path)：    将url路径转换成本地路径"""
