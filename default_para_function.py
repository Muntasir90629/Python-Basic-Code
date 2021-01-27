

# def myfnc(y=10):
#     print(y)
    
# x=20

# myfnc(x)

# myfnc()


# def myfnc(x,y=10,z=10):
#     print("x = ",x,"y= ",y,"z=",z)
    
# x=2
# y=3
# z=6

# myfnc(x,y,z)

# myfnc(x,y)

# myfnc(x)

# def myfake(x,z,y=10):
#     print("x=",x,"y=",y,"z=",z)
    
# myfake(x=1,y=2,z=5)
# a=5
# b=6

# myfake(x=a,z=b)
# a=1
# b=2
# c=3
# myfake(y=a,z=b,x=c)
def add_number(numbers):
    Result=0
    for i in numbers:
        
        Result=Result+i
        
    return Result
    


li=[]
i=0
while True:
    
    stg=input("Enter the numbers")
    stg=int(stg)
    if stg==0:
        break
    
    li.append(stg)
    
    i=i+1



Result=add_number(li)

print(Result)


    
    
    
    