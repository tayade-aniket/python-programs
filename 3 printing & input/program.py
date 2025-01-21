# Python is Case Sensetive Language. That's why following both values are two different from eachother.
str1 = "Apple"
str2 = "apple"

print(str1)
print(str2)

# If we use numbers in format of string it will considered as string.
num = '99'

print(num)
print(type(num))

# Input() - It is used for getting input from user.

input("Enter Your Name : ")

# but above line of code help to get input but won't able to return that input. so we can store it in a variable.
name = input("Enter Your Name : ")
print("Welcome", name)

# Let's take another example to understand this better.
age = input("Enter Your Age : ")
print("Your Age is : ", age)
