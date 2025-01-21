# Tuple
# tuple is created using () 
# tuple is ordered and indexed 
# tuple elements can be accessed using its index value within [] 
# tuple is immutable(which can not be modified) 

tup=(23,78,90,56,75)

print(tup)
print(type(tup))

# using index number print elements
print(tup[2])

# getting sub-tuple
print(tup[0:3] )

myTup = tup + tup
print(myTup)

# Tuple | Methods
# 1. count-It returns the frequencies of the given element 
print(tup.count(23))

# 2. index-It return the lowest index of given element 
print(tup.index(90))
