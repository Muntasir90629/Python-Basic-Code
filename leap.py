year=input("Enter the year")

year=int(year)

# if year%4==0:
    
#     if year % 100==0:
#         if year%400==0:
#             print("yes")
#         else:
            
#             print("No")
            
            
#     else:
#         print("yes")
        
        
# else:
    
#     print("no") 



if year%4 !=0:
    print("No")

else:
    if year  %100 !=0:
        print("yes")
        
    else:
        if year%400!=0:
            print("No")
        else:
            print("yes")
        
        
        