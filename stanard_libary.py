import os 
os.rename("newfile.txt","123.txt")
os.remove("123.txt")
os.listdir("C:\\Users\\iweut\Documents\\Python Scripts\\Test")        #显示目录中的文件
fls = os.listdir("C:\\Users\\iweut\Documents\\Python Scripts\\Test")
for f in fls:
    print(f)

os.open("C:\\Users\\iweut\Documents\\Python Scripts\\Test")
cur_path = os.getcwd()
print(cur_path)

os.chdir(os.pardir) # os.pardir的功能是获得上一级目录
os.getcwd()
os.chdir("C:\\Users\\iweut\Documents\\Python Scripts\\Test")  
os.getcwd()

os.removedirs("C:\\Users\\iweut\Documents\\Python Scripts\\Test")  # 要删除某个目录，那个目录必须是空的
os.makedirs("os_module")
os.getcwd()
os.chdir("os_module")
os.getcwd()
os.listdir(os.getcwd())
new_path = os.getcwd()
os.removedirs(new_path) # PermissionError: [WinError 32] 另一个程序正在使用此文件，进程无法访问。: 'C:\\Users\\iweut\\Documents\\Python Scripts\\Test\\os_module'
os.chdir(os.pardir())
os.removedirs("C:\\Users\\iweut\\Documents\\Python Scripts\\Test\\os_module")

os.chdir(r"C:\Users\iweut\Documents\Python Scripts\Test")  # 在r" "中的，都是被认为原始字符了
os.getcwd()

#使用python打开其他软件的方法
os.system(r'"C:\Program Files\MATLAB\R2013a\bin\matlab.exe"') # 注意读入程序时，需要将程序路径用引号再包括起来
os.system('"C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe"') # 注意读入程序时，需要将程序路径用引号再包括起来

#使用python打开网页的两种方法
import os 
import webbrowser
webbrowser.open("https://cn.bing.com/") # 使用系统默认程序打开指定网页
os.system(r'"C:\Program Files\internet explorer\iexplore.exe" https://www.baidu.com/')  #可以用指定程序打开指定网页

# 打开程序之后的语句后面 没有空格会提示错误：文件名、目录名或卷标语法不正确。
os.system(r'"C:\Program Files\internet explorer\iexplore.exe"https://www.baidu.com/')  

#heapq模块  堆（英语：heap)，是计算机科学中一类特殊的数据结构的统称。
import heapq
hp = []
heapq.heappush(hp, 1)
heapq.heappush(hp, 30)
heapq.heappush(hp, 10)
heapq.heappush(hp, 9)
heapq.heappush(hp, 50)
heapq.heappush(hp, 28)
print(hp) # 查看堆的数据时，显示的是一个有一定顺序的数据结构。按照完全二叉树(Full Binary Tree)的方式排列
hp
heapq.heappop(hp) # 从heap堆中删除了一个最小元素，并且返回该值
heapq.heappush(hp, 1)
heapq.heappush(hp, 30)
heapq.heappush(hp, 10)
heapq.heappush(hp, 9)
heapq.heappush(hp, 50)
heapq.heappush(hp, 28)
hp
# 将列表转换为堆
hp_lst = [1, 30, 9, 50, 28, 10, 9, 30, 28, 50, 10]
heapq.heapify(hp_lst) 
hp_lst # hp_lst与最初创建的列表不同，但是与hp的元素相同，但是heap的排列顺序不同 why?

from collections import deque
lst = [1, 2, 3, 8, 12]
dq_lst = deque(lst)
dq_lst.append(5)
dq_lst.appendleft(20)
dq_lst
dq_lst.rotate(3)  # 右移3位
dq_lst
dq_lst.rotate(-2) # 左移两位
dq_lst

#calendar模块
import calendar
cal = calendar.month(2018,9)
print(cal)
year = calendar.calendar(2018, w=2, l=1, c=6, m=4) #w每日宽度间隔，l每星期行数，c列之间的间隔距离，m每行显示的月数
print(year)
calendar.isleap(2018) #判断是否是闰年
calendar.leapdays(1991,2018)
print(calendar.month(2018, 8, w=2, l=2))
calendar.monthcalendar(2018,8) # 显示月的嵌套列表
calendar.month(2018, 8) # 显示一个字符串列表
calendar.weekday(2018, 8, 18) #显示5 ，表示星期六

#time模块 datetime模块作为补充，包括date类，time类，datedelta类等
import time
time.time()
time.localtime() # 显示当前时间tuple
time.gmtime()    # 显示Greenwich Mean Time，GMT
t = time.localtime(1534579091.0) # 以时间戳为参数
time.asctime(t)  # 参数必须是时间元组
time.ctime() # 当前时间'Sat Aug 18 16:02:37 2018'

today = time.strftime("%y/%m/%d")
today
time.strptime(today, "%y/%m/%d") #显示：time.struct_time(tm_year=2018, tm_mon=8, tm_mday=18, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=230, tm_isdst=-1)

# urllib
import urllib.request
import urllib3
website = urllib.request.urlopen("https://www.python.org/")
print(website.read())
website.info()
website.getcode()
website.geturl()

#json 模块
import json
json.__all__ # 结果为：['dump', 'dumps', 'load', 'loads', 'JSONDecoder', 'JSONDecodeError', 'JSONEncoder'] dump表示内存信息转存
data = [{"name":"RankeTao", "lang":("python", "C++"), "age":18},{"name":"Todd", "lang":("english", "french"), "age":28}]
print(data)
json_data = json.dumps(data) # encoding: dumps()  python-->json
print(json_data) # 结果为：[{"name": "RankeTao", "lang": ["python", "C++"], "age": 18}, {"name": "Todd", "lang": ["english", "french"], "age": 28}]
type(data) # list
type(json_data) # str

new_data = json.loads(json_data) # decoding: loads() 需要注意的是，解码之后，并没有将元组还原。
print(new_data) # 结果为：[{'name': 'RankeTao', 'lang': ['python', 'C++'], 'age': 18}, {'name': 'Todd', 'lang': ['english', 'french'], 'age': 28}]
# 美化输出
data_j = json.dumps(data, sort_keys=True, indent=2) # sort_keys=True意思是按照键的字典顺序排序，indent=2是让每个键值对显示的时候，以缩进两个字符对齐
print(data_j)

# 相互转化关系
python_to_json = ["dict-->object","list,tuple-->array","str,unicode-->string","int,long,float-->number","True-->true","False-->false","None-->null"]
json_to_python = ["object-->dict","array-->list","string-->unicode","number(int)-->int,long","number(real)-->float","true-->True","false-->False","null-->None"]

import tempfile
f = tempfile.NamedTemporaryFile(mode='w+')
json.dump(data, f)
f.flush() # flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。
f_rd = open(r'C:\Windows\Temp\tmpop4j77po', "r").read()
print(f_rd)