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
fib(6)

