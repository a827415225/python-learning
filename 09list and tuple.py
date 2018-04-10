#list 
classmates = ['tom','bob','tim']
print(len(classmates))
print('classmates=',classmates)
print('classmates[0]=',classmates[0])
print('#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素')
print('classmates[-1]=',)

print('')

print('#往list中追加元素到末尾')
print('classmates.append(\'jim\')')
classmates.append('jim')
print(classmates)

print('')

print('#把元素插入到指定的位置，比如索引号为1的位置')
print('classmates.insert(1,\'jack\')')
classmates.insert(1,'jack')
print(classmates)

print('')

print('#删除list末尾的元素，用pop()方法')
print('classmates.pop()')
classmates.pop()
print(classmates)

print('')

print('#要删除指定位置的元素，用pop(i)方法，其中i是索引位置')
print('classmates.pop(1)')
classmates.pop(1)
print(classmates)

print('')

print('要把某个元素替换成别的元素，可以直接赋值给对应的索引位置')
print('classmates[1]=123')
classmates[1]=123
print(classmates)

print('')
print('list元素也可以是另一个list，')
print('s=[\'a\',\'b\',[\'c\',\'d\'],\'e\']')
s=['a','b',['c','d'],'e']
print(s)

print('len(s)=',len(s))

print('p = [\'asp\', \'php\']')
print('s = [\'python\', \'java\', p, \'scheme\']')
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']

print('s=',s)
print('#要拿到\'php\'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。')

print('')
print('')
print('')


#tuple
print('tuple和list非常类似，但是tuple一旦初始化就不能修改')
print('tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来')
print('但是，要定义一个只有1个元素的tuple，这么定义t = (1,)')

print()

print('list用[]定义，tuple用()定义')

print('“可变的”tuple：')
print('t = (\'a\', \'b\', [\'A\', \'B\'])')
print('其中tuple的第二个元素的内容是可变的。')



print('#练习题')
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print('L=',L)
print(L[0][0])
print(L[1][1])
print(L[2][2])


