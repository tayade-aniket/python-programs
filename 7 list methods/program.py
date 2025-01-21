myList = [12, 34, 56, 78, 90, 32, 34, 54, 99] 

# 1.append- To add the eleemnt at the end of the list 
myList.append(101)
print(myList)

# 2. insert-To add the element at the specific index 
myList.insert(3,"apple") 
print(myList)

# 3.extend-To add multiple elements at the end of the list 
myList.extend([91,92,94,95]) 
print(myList)

# 4.pop()-It removes the given index element and returns the removed element.
# By default it removes last index element 
myList.pop() 
print(myList)

# 5.remove-Element wise remove 
myList.remove(92) 
print(myList)

# 6. sort-It does the sorting. 
# By default sorting is done in ascending order.To do sorting in descending order we require to pass arguemnt 
# reverse=True
new_list=[12, 98, 78, 32, 34, 54, 91, 94, 95] 
new_list.sort() 
print(new_list)

new_list.sort(reverse=True) 
print(new_list)


fruits = ['apple','Mango','Orange','cucumber'] 
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

# 7. index- It returns the lowest index value of given element 
print(new_list)
print(new_list.index(98))

# 8.count-It returns the no of frequencies of the given element 
nums = [12,13,12,13,14,15,16,17,13] 
print(nums)
print(nums.count(13))

# 9.reverse-It reverse the list
nums.reverse()
print(nums)

# 10. copy()-To copies one list to another list 
new_num = nums.copy()
print(new_num)

# 11. clear-It removes all elements from the list 
new_num.clear()
print(new_list)