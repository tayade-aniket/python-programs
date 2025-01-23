# WAP to display the highest number from the inputs given by user 5 times.use for loop 

new_List=[]

for i in range(5):
    num=int(input("Enter a Value : "))
    new_List.append(num)

print("Original List : ",new_List)

new_List.sort(reverse=True)
print("Sorted List", new_List)
print("Highest Number is : ", new_List[0])