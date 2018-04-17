print('1+1')
a = list(range(1,11))
print(a)


L = []
for x in range(1,11):
	L.append(x*x)

print(L)
#list 不仅可以用来生成规律的等差数列，还可以用来生成其他的规律型数列
#但是上面的表达太麻烦，所以由此产生了列表生成式

M = [x*x for x in range(1,11)]
print(M)

N =  [3*x*x+x+1 for x in range(1,11)]
print(N)

O = [x*x for x in range(1, 11) if x % 2 == 0]
print(O)

P = [m+n for m in 'ABC' for n in 'XYZ']
print(P)

#Q = [m*n for m in 'ABC' for n in 'XYZ']
#print(Q)

import os
R = [d for d in os.listdir('.')]
print(R)

#dict
d = {'x':'a', 'y':'b', 'z':'c'}
for k, v in d.items():
	print(k,'=',v)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
S = [k + '=' + v for k, v in d.items()]

#注意到上面的两个细节，上面的36行print函数中k和v之间只有等号，
#但是下面的下面的39行k和v之间多了加号，这个加号的存在就相当于
#36行中的逗号。

L = ['Hello', 'World', 'IBM', 'Apple']
T = [s.lower() for s in L]
print(T)

x = 'abvc'
y = 123
print(isinstance(x,str))
print(isinstance(y,str))

#练习题
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]



# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

