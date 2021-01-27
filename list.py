list=[1,2,3,4,5,6,7,8,9,10]

print(list)

print("ENTER THE NUMBER you want to ENTER THE LIST")

c=input("PRESS THE THE KEY :  ")

c=int(c)

l=[]


i=1


while i <=c:
    
    print
    
    j=input("Insert number {}: ".format(i))
    
    j=int(j)    
    l.append(j)
    i+=1


for r in l:
    
    print(r)


