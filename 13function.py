#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#call function
a=-3
print(abs(a))

print(max(2,1))

a = abs
print(a(-1))


a=100
b=hex(a)
c=str(b)
print(a)
print(b)
print(c)
print('type(a)=',type(a))
print('type(b)=',type(b))
print('type(c)=',type(c))


#define function
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-199))



print('''如果你已经把my_abs()的函数定义保存为abstest.py文件了，
那么，可以在该文件的当前目录下启动Python解释器，
用from abstest import my_abs来导入my_abs()函数，
注意abstest是文件名（不含.py扩展名）''')


print('from x import y')


print('如果想定义一个什么事也不做的空函数，可以用pass语句')
age=11
if age >= 18:
    pass

print('调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError')
#my_abs(1,2)
#abs(1,2)
print('我们会发现同样的问题，自定义的函数与官方函数的TypeErr还是有一定的差别的。问题是我们自己写的函数不完善，完善的写法如下所示。')
# def my_abs(x):
    # if not isinstance(x, (int, float)):
        # raise TypeError('bad operand type')
    # if x >= 0:
        # return x
    # else:
        # return -x

#返回多个数值
print('返回多个数值')
print('import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。')
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny  
x, y = move(100, 100, 60, math.pi / 6)
print(x, y) 
print('实际上返回值是一个tuple')   
r = move(100, 100, 60, math.pi / 6)
print(r)



import math
def quadratic(a,b,c):
    x = math.sqrt(a*x*x+b*x+c=0)
    return x

r=quadratic(1,2,1)
print(r)