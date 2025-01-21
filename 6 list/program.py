# list 
# list is created using [] 
# list can store multiple values 
# list is ordered and indexed # list elements can be accessed using index inside [] 
# list is mutable (which can be modified)

my_list = [122, 63, 89, 71, 90]

print(my_list)
print(type(my_list))

# accessing the element from List
print(my_list[0])

# Changing values from index
my_list[1] = 100
print(my_list)

# index 
# In python indexing starts from zero from left to right 
# In python indexing starts from -1 from right to left

new_list = [191, 34, 55, "Apple", True, 33.34]

print(new_list)
print(new_list[4])
print(new_list[-3])

# subsetting
newList=[10,11,19,45,89,90,46,93,76,67]

print(newList[0:4])
print(newList[-5:-1])

# we can also can use steps to get some specific values from list for that use - (start,stop,[step]) 
# step is optional.By default step value is +1 

print(newList[0:5:2])

# dir()- list of directory 
dir(newList) 