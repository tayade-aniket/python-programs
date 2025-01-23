# WAP to display whether the given number is divisible by 2 or 3 or 5 uisng Multiple If conditions

num = int(input("Please Enter a Number : "))

if num%2 ==0:
    print("Given Number is Divisible by 2")
elif num%3==0:
    print("Given Number is Divisible by 3")
elif num%5==0:
    print("Given Number is Divisible by 5")
else:
    print("Given Number is Neither divisible by 2,3 or 5")