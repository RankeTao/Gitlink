""" _formats = {'ymd' : '{d.year}-{d.month}-{d.day}', 'mdy' : '{d.month}/{d.day}/{d.year}', 'dmy' : '{d.day}/{d.month}/{d.year}'}

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

d = Date(2018, 8, 15) """

""" class Spring(object):
    season = "the Spring of class"
#不管是实例还是类，都用__dict__来存储属性和方法，可以笼统地把属性和方法称为成员或者特性，
#用一句笼统的话说，就是__dict__存储对象成员。但，有时候访问的对象成员没有存在其中,就返回错误
# AttributeError: 'A' object has no attribute 'x'
Spring.__dict__  # 对于类Spring的__dict__属性，可以发现，有一个键'season'，这就是这个类的属性；其值就是类属性的数据。
Spring.__dict__['season'] # Spring.__dict__['season']就是访问类属性
Spring.season
s = Spring()
s.__dict__  # 结果为: {} 
s.season    # 结果为: 'the Spring of class' 这个其实是指向了类属性中的Spring.season，至此，我们其实还没有建立任何实例属性呢
s.season = "the Spring of instance" 
s.__dict__  # 结果为：{'season': 'the Spring of instance'} 这样，实例属性里面就不空了
s.__dict__['season']
s.season    # 结果为：'the Spring of instance'  建立的实例属性和上面的那个s.season只不过重名，并且把它“遮盖”了
Spring.__dict__['season'] # 结果为：'the Spring of class'   Spring的类属性没有受到实例属性的影响
Spring.__dict__
Spring.season
del s.season
s.__dict__  # 结果为: {} 
s.season    # 结果为: 'the Spring of class'
#当然，可以定义其它名称的实例属性，它一样被存储到__dict__属性里面
s.lang = "python"
s.__dict__  # 结果为：{'lang': 'python'} 这样做仅仅是更改了实例的__dict__内容，对Spring.__dict__无任何影响

Spring.lang             # 返回错误 E1101:Class 'Spring' has no 'lang' member
Spring.__dict__['lang'] # 返回错误

Spring.flower = "peach" # 增加Spring class 的flower属性
Spring.__dict__
Spring.__dict__['flower']

s.__dict__  # 结果仍为：{'lang': 'python'} 
s.flower    # 结果为：'peach'
#总结：属性都是可以动态变化的，可以随时修改和增删。 """

class Spring(object):
    def tree(self, x):
        self.x = x
        return self.x

Spring.__dict__
Spring.__dict__['tree']

t = Spring()
t.__dict__
t.tree("willow")
t.__dict__
# 印证了实例t和self的关系，即实例方法(t.tree('xiangzhangshu'))的第一个参数(self，但没有写出来)绑定实例t，
# 透过self.x来设定值，即给t.__dict__添加属性值。
class Spring(object):
    def tree(self, x):
                      #这里没有将x赋值给self的属性，直接return
        return x

s = Spring()
s.tree("birch")
s.__dict__            # 所以这里的结果就是 {}
# 不管是类还是实例，其属性都能随意增加。
# __slots__能够限制属性的定义，但是这不是它存在终极目标，它存在的终极目标更应该是一个在编程中非常重要的方面：优化内存使用。

class Spring(object):
    __slots__ = ("tree", "flower")

dir(Spring) # 没有了__dict__属性

Spring.__slots__ # ('tree', 'flower')  类Spring有且仅有两个属性。

t = Spring()
t.__slots__   # 实例化之后，实例的__slots__与类的完全一样，这跟前面的__dict__大不一样了。

Spring.tree = "willow" # 通过类，先赋予一个属性值。
t.tree = "birch" # 检验一下实例能否修改这个属性，报错： AttributeError: 'Spring' object attribute 'tree' is read-only。
t.tree # 'willow'
#不能用实例属性来修改，只能通过类属性修改
Spring.tree = "birch"
t.tree # 'birch'

t.flower = "rose"  # 但是对于没有用类属性赋值的，可以通过实例属性
Spring.flower # <member 'flower' of 'Spring' objects>
Spring.flower = "daisy" # 通过类属性赋值
t.flower  # 实例属性也被改变

t.fence = "bambo" # 返回错误 AttributeError: 'Spring' object has no attribute 'fence' 这里试图给实例新增一个属性，也失败了
Spring.water = "green" # 给类增加了一个water属性，但是没有添加进__slots__里面
Spring.water # 'green'
dir(Spring)
# 看来__slots__已经把实例属性牢牢地管控了起来，但更本质是的是优化了内存。诚然，这种优化会在大量的实例时候显出效果。