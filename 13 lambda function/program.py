# lambda-using lambda keyword we can create function.It is nameless function.
# It is also called short function. # It can take n number of arguments but can take only one expression

# Syntax
# lambda arguements:Expression 

square = lambda n:n**2

print(square(5))

# filter- It requires 2 arguements.one is function and another one is iterator 
my_List = [23,45,67,89,90,12,34,79] 

# Noramal Zindagi
new_List = []
for i in my_List:
    if i % 2 == 0:
        new_List.append(i)

print(new_List)

# Mentoss Zindagi
#printing Even Numbers
print(list(filter(lambda x:x%2==0,my_List)))

# printing Odd Numbers
print(list(filter(lambda x:x%2!=0,my_List)))

# map-It requires two arguements.one is function and another is iterator
# Here we want the product of given list elements

# Normal Zindagi
num_List=[2,5,8,9,10]
result_List = []
for i in my_List:
    result_List.append(i)

print(new_List)

# Mentoss Zindagi
print(list(map(lambda x:x**2,num_List)))


# function- function is used standalne.It always comes with small parenthesis.Arguements can be passed inside function 
# ex- print(),len() 

# methods- methods is used along with its object.It always comes with small parenthesis. 
# It is called with dot(.) operator along with its object name. 
# Arguements can be passed inside methods 
# ex- append(),insert() of list # attribute- attribute is used along with its object.It does not come with arguements.
# It is getting used with dot(.) operator along with its object name. 

# Arguements can nnot be passes inside attributes 
# ex-math.pi 
# arguements-it is passed inside functions and methods 