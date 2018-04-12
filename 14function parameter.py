#位置参数
def power(x):
    return (x*x)

print(power(5))

import math

def powern(x,n):
    y = 1
    while n > 0:
        y=y*x
        n = n - 1
    return y
    # return (math.pow(x,n))
print(powern(5,3))



#默认参数
def powern2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(powern2(5))
print(powern2(5,2))


print('''默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度。''')

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

def enrolll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enrolll('liuyong','abc')

# 定义一个函数，传入一个list，添加一个END再返回：

# def add_end(L=[]):
    # L.append('END')
    # return L
# 当你正常调用时，结果似乎不错：

# >>> add_end([1, 2, 3])
# [1, 2, 3, 'END']
# >>> add_end(['x', 'y', 'z'])
# ['x', 'y', 'z', 'END']
# 当你使用默认参数调用时，一开始结果也是对的：

# >>> add_end()
# ['END']
# 但是，再次调用add_end()时，结果就不对了：

# >>> add_end()
# ['END', 'END']
# >>> add_end()
# ['END', 'END', 'END']
# 很多初学者很疑惑，默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。

# 原因解释如下：

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
print('定义默认参数要牢记一点：默认参数必须指向不变对象！')



#可变参数
#复杂的方法
# # def calc(numbers):
    # # sum = 0
    # # for n in numbers:
        # # sum = sum + n * n
    # # return sum
# # 但是调用的时候，需要先组装出一个list或tuple：
# # >>> calc([1, 2, 3])
# # 14
# # >>> calc((1, 3, 5, 7))
# # 84

#简单的方法
# # def calc(*numbers):
    # # sum = 0
    # # for n in numbers:
        # # sum = sum + n * n
    # # return sum
# # >>> calc(1, 2)
# # 5
# # >>> calc()
# # 0

print('Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去')
# # >>> nums = [1, 2, 3]
# # >>> calc(*nums)
# # 14
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n*n
    return sum

    
print(calc(1))
print(calc(1,2))
print(calc(1,2,3))



#关键字参数
print('可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。')
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person('Michael', 30)
#也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
person('Adam', 45, geer='M', job='Engineer')#一个错误的参数也可以传入
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，
#我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
#我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
#其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数。

print('对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。')
print('仍以person()函数为例，我们希望检查是否有city和job参数：')
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print('如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：')
def person1(name,age,*,city,job):
    print(name,age,city,job)

print('和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。')
person1('Jack', 24, city='Beijing', job='Engineer')
#person1('Jack', 24, cit1='bj',job='Engineer')#错误的参数传输会报错
#person1('Jack', 24,job='Engineer')#不可缺参数

print('如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：')
#意思就是，如果存在一个可变参数*arg了，那就不再需要一个单独的*了。
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：   
# >>> person('Jack', 24, 'Beijing', 'Engineer')
# Traceback (most recent call last):
  # File "<stdin>", line 1, in <module>
# TypeError: person() takes 2 positional arguments but 4 were given
# 由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。   


#命名关键字参数可以有缺省值，从而简化调用：
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)

person3('Jack', 24, job='Engineer')





#参数组合
#必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用

#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a, b, c=0, *, d, **kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

f1(1, 2)

f1(1, 2, c=3)

f1(1, 2, 3, 'a', 'b')

f1(1, 2, 3, 'a', 'b', x=99)

f2(1, 2, d=99, ext=None)

#任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
print('任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。')




#练习题
def product(x, *arg):
    val=x
    for i in arg:
        val = val*i
    return val

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')