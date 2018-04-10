# age1=input('input your age:')
# age=int(age1)
# if age >= 18:
    # print('your age is %d, you are a adult' % age)
    # print('end')
# else:
    # print('your age is %d, you are a teenager' % age)

    
# age1=input('input your age:')
# age=int(age1)
# if age >= 18:
    # print('your age is %d, you are a adult' % age)
# elif age >=6:
    # print('your age is %d, you are a teenager' % age)  
# else:
    # print('your age is %d, you are a kid' % age) 
    
# x=int(input('input a number:'))   
# if x:
    # print('True')

a=float(input('input height:'))
b=float(input('input weight:'))
bmi=b/a/a;
if bmi <18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')