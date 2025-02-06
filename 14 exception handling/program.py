# Python Exception Handling handle errors that occur during the execution of a program. Exception handling allows to
# respond to the errors, instead of crashing the running program. It enables you to catch and manage errors, making
# your code more robust and user-friendly.

# Example : Trying to divide a number by Zero will cause an exception

# num1 = int(input("Enter First Number : "))
# num2 = int(input("Enter Second Number : "))

# result = num1 / num2

# print(result)

# Above program will gives us the error like - ZeroDivisionError
# Instead of stopping our program we can use following senario

# try : 
#     result = num1 / num2
# except ZeroDivisionError:
#     print("Can't be divided by Zero")

# But what is we pass any one value as a character, then it will display us the ValueError 
# in such condition we can update our code


# try:    
#     num1=int(input("Enter a number :"))    
#     num2=int(input("Enter a number :"))    
#     result=num1/num2    
#     print(result) 
# except (ZeroDivisionError,ValueError):    
#     print("Not divisible") 


# We also can use else part in the try_except block
# try:    
#     num1=int(input("Enter a number :"))    
#     num2=int(input("Enter a number :"))    
#     result=num1/num2    
#     print(result) 
# except (ZeroDivisionError,ValueError):    
#     print("Not divisible") 
# else:    
#     print("Division Successful") 


# And the last part of try_except is finally block
try:    
    num1=int(input("Enter a number :"))    
    num2=int(input("Enter a number :"))    
    result=num1/num2    
    print(result) 
except (ZeroDivisionError,ValueError):    
    print("Not divisible") 
else:    
    print("Division Successfull")
finally:    
    print("Operation Completed")