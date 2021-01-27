terminate=False

while not terminate:
    
    number1=input("Enter the first number")
    number1=int(number1)
    number2=input("Enter the second number")
    number2=int(number2)
    
    
    while True:
        
        operation=input("please enter add/sub or quit to exit")
        
        if operation=="quit":
            
            terminate=True
            break
        
        if operation not in ["add","sub"]:
            print("Unkown operation !")
            continue
        
        if operation=="add":
            print("the result is",number1+number2)
            break
        
        if operation=="sub":
            
            print("Result is ",number1-number2)
            break
        
    