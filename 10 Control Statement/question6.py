# Nested if elif

age=int(input("Enter ur age :")) 

if(age>=18):    
    ch=input("Do u driving license y\n")    
    if ch=="y":        
        print("You can drive")    
    else:        
        print("You can apply for driving license") 
elif(age>=12):    
    ch=input("Do u driving license y\n")    
    if ch=="y":        
        print("You can drive under guardian custody")    
    else:        
        print("You can apply for license under guarding category") 
else: print("you are not eligible to drive") 