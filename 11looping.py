a=[12,34,56,78]
for i in a:
    print(i)

    
print(list(range(5)))

sum=0
for i in list(range(101)):
    sum+= i
print(sum)

#while
sum=0
n=99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


#break
sum=0
n=99
while n > 0:
    sum = sum + n
    n = n - 2
    if n < 3:
        break
print(sum)


#continue
sum=0
n=9
while n > 0:
    sum = sum + n
    n = n - 2
    if n == 3:
        continue
    print(n)
#print(sum)