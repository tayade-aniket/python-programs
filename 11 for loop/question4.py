# WAP to create a new list which consists only even numbers from the existing list.use for loop 
my_list=[11,13,14,16,18,20,22,24,21] 

new_List=[]

for i in my_list:
    if i%2==0:
        new_List.append(i)
    
print(new_List)