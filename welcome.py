print("Enter your name ")

name=input("type here please")

print("welcome to python ,",name,"!" )

print("Now we want to do some operation")

print("Enter two value")

d=input("enter first number")
d=int(d)

e=input("Enter second number")

e=int(e)
f=input("input the job u want to done ")

def sub(a,b):
    
    return a+b

def min(a,b):
    
    return a-b

def mul(a,b):
    
    return a*b


if  f=='h':
    print(sub(d,e)) 
    
elif f=='j':
    print(min(d,e))
    
else:
    
    print(mul(d,e))
    
    
    