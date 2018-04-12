#递归函数
def fact(n):
	if n == 1:
		return 1
	return n*fact(n-1)

print('fact(6)=',fact(6))
print('fact(5)=',fact(5))
print('fact(4)=',fact(4))
print('fact(3)=',fact(3))
print('fact(2)=',fact(2))
print('fact(1)=',fact(1))


#尾递归
def fact(n):
	return fact_iter(n,1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1, num*product)



	
#练习题
def move(n,a,b,c):
	if n==1:
		print(a,'-->', c)
	else:
		move(n-1,a,c,b)
		move(1,a,b,c)
		move(n-1,b,a,c)

move(3,'A','B','C')