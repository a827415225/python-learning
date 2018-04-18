#生成器
#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，
#列表容量肯定是有限的。我们是否可以在循环的过程中不断推算出后
#续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在
#Python中，这种一边循环一边计算的机制，称为生成器：generator。

#方法一：只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
print(g)
#通过next()函数获得generator的下一个返回值：
print(next(g))
print(next(g))

#正确的方法是使用for
for x in g:
	print(x)

def fib(max):
	n, a, b =0, 0, 1
	while n < max:
		print(b)
		a, b = b ,a + b
		n = n + 1
	return 'done'


# 注意，赋值语句：

# a, b = b, a + b
# 相当于：

# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
print('fib(6)=')
fib(6)


#函数定义中包含yield关键字，这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

f = fib(6)
print(f)

#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。



#用for循环调用generator时，发现拿不到generator的return语句的返回值。
#如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration
#的value中：

# g = fib(6)
    # while True:
        # try:
            # x = next(g)
            # print('g:', x)
        # except StopIteration as e:
            # print('Generator return value:', e.value)
            # break

            
# def triangles():
    # L=[1]
    # while True:
        # yield L
        # L.append(0)
        # L = [L[x-1]+L[x] for x in range(len(L))]
def triangles():
    L=[1]
    while True:
        yield L
#        print(results)
        M = L + [0]
#        print(results)
        L = [M[x-1]+M[x] for x in range(len(M))]

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
#    print(results)
    print(t)
#    results = results+t
    results.append(t)
#    print(results)
    n = n + 1
    if n == 10:
        break



if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:

    print('测试通过!')
else:
    print('测试失败!')
    
    
#迭代器

# 凡是可作用于for循环的对象都是Iterable（可迭代对象）类型；
# 凡是可作用于next()函数的对象都是Iterator（迭代器）类型，它们表示一个惰性计算的序列；

# Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不
# 断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是
# 一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需
# 计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。

from collections import Iterable
from collections import Iterator