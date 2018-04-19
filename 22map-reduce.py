#map
#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数
#依次作用到序列的每个元素，并把结果作为新的Iterator返回。

#注意是作为Iterator来返回的，所以返回的东西不能直接显示，它是一个惰性序列
#因此需要list将结果计算出来，并返回一个list
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
print('r=',r)
print('list(r)=',list(r))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

#上式实现与map函数相同功能，但是却不能一眼看出功能。

#map，将list所有数字转为字符串

print(list(map(str,[1,2,3,4,5,6,7])))



#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收
#两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


#实现求和运算。
def add(x, y):
    return x + y

print(reduce(add ,[1,2,3,4,5]))

#把序列[1,3,5,7,9]变成13579，
def fn(x,y):
    return x*10+y

print(reduce(fn, [1, 3, 5, 7, 9]))


#str转为int的函数
def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

print(reduce(fn, map(char2num,'13579')))

#整理成一个str2int函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))   

    
#练习题1
a=0
def normalize(name):
    name.lower()

    return name[0].upper()+name[1:].lower()
    
    

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



#练习题2
def prod(L):
    def chengf(x,y):
        return x*y
    return reduce(chengf,L)


#测试   
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
    

#练习题3
def str2float(s):
    dot = s.index('.')
    s1 = s[:dot]+s[dot+1:]
    def f1(x, y):
        return x*10+y    
    def tofloat(z):
        digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[z]
    return reduce(f1,map(tofloat,s1))/pow(10,len(s1)-dot)    
    
    
#测试
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')