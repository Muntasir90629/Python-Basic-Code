while  True:
    n=input("please enter postive number : ")
    n=int(n)
    if n<0:
        print("we only allow positve number ,please try again")
        
    if n==0:
        break
    
    print("square of ",n,"is",n*n)
    