# WAP to display whether the given number is divisible by 2 or 3 or 5 
# Here we can use AND, OR as a Memebership operator

num = int(input("Please Enter Your Number : "))

if num%2==0 or num%3==0 or num%5==0:
    print("Given Number is Divisible by 2, 3 and 5")
else:
    print("Given number is not divisible by 2, 3 and 5")