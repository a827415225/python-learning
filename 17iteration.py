#list或者tuple
a=[1,2,3,4]
for i in a:
    print(i)

#dict
b={'ab':1,'bc':2,'cd':3}
for key11 in b:
    print(b[key11])

for value in b.values():
    print(value)

for k,v in b.items():
    print(k)
    print(v)

#字符串
for ch in 'ABC':
    print(ch)
    
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)
    
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
    
    
    
#练习题
def findMinAndMax(L):
#    return (L.max(),L.min())
    if L == None:
        return (None,None)
    max = None
    min = None    
    for i in L:
        if max < i:
            max = i
        if min > i:
            min = i
    return (max,min)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
