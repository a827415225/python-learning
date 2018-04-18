#变量可以指向函数
print(abs(-10))

print(abs)

print('abs(-10)是函数调用，而abs是函数本身。')

x = abs(-10)
print(x)

f = abs
print(f)

print('函数本身也可以赋值给变量，即变量可以指向函数')

print(f(-10))

print('变量f现在已经指向了abs函数本身。直接调用abs()函数和调用变量f()完全相同。')

#
#通过以上分析，我门可以说函数名其实就是指向函数的变量。

#如果
#abs = 10
#print(abs(-10))
print('把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！')


#由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量
#的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

# import builtins
# builtins.abs = 10




#传入函数

#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。


def add(x, y, f):
    return f(x)+f(y)

print(add(-3, -4, abs))











