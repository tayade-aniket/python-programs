name = input("Enter Your Name : ")
print("Welcome", name)

# Let's take another example to understand this better.
age = input("Enter Your Age : ")
print("Your Age is : ", age)

# But what if we want to perform any arithmetic operation with age. can we perform it? let's try.
# result = age + 10
# print(result)

# No. It's not possible it with return error like - TypeError: can only concatenate str (not "int") to str.
# First understand why this happens. 
print(type(age))

# If we use type() then we get <class 'str'> that means it returns age with type String. and we cannot perform any arithmetic operation with String.
# For resolve this we need to use Type Casting. Type Casting is the method to forcefuly change the type of any value.

# int()-It converts another data type into integer

num1 = 5.5

print(num1)
print(type(num1))
print(int(num1))
print(type(int(num1)))

num2 = True

print(num2)
print(type(num2))
print(int(num2))
print(type(int(num2)))

# float()-It converts another data type into float 

num3 = 199
print(num3)
print(type(num3))
print(float(num3))
print(type(float(num3)))

# str()-It converts another data type into str 

num4 = 55
print(num4)
print(type(num4))
print(float(num4))
print(type(float(num4)))


# Now we can convert our input in any type using Type Casting
# Let's try

age = int(input("Enter Your Age : "))
print(age)
print(type(age))
