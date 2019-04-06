#e.g 1
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)
    
    def __str__(self):
            return '({0.x!s}, {0.y!s})'.format(self)

p = Pair(3, 4)
"""自定义__repr__() 和__str__() 通常是很好的习惯，因为它能简化调试和实例
输出。例如，如果仅仅只是打印输出或日志输出某个实例，那么程序员会看到实例更加
详细与有用的信息。
如果__str__() 没有被定义，那么就会使用__repr__() 来代替输出。"""

#e.g 2
_formats = {'ymd' : '{d.year}-{d.month}-{d.day}', 'mdy' : '{d.month}/{d.day}/{d.year}', 'dmy' : '{d.day}/{d.month}/{d.year}'}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __format__(self, code):
        if code == '' :
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

d = Date(2018, 8, 15)

        