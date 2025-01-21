# Dictionary (dict) 
# dict is created using {} in key value pair 
# dict values can be accessed using key 
# dict in unindexed # dict is mutable 

book={"Python":450,"ML":680,"HTML":350} 
# keys are Python,ML & HTML 
# Values are 450,680,350 

emp={101:"Abc",102:"Def",103:"Pqr",104:"xyz"} 
print(emp)
print(type(emp))

book={"Python":450,"ML":680,"HTML":350} 
print(book["ML"])

book["ML"]=880 
print(book)

# 1. keys-It returns all keys 
print(book.keys())

# 2. values-It returns all values 
print(book.values())

# 3. items-It returns dict in the form of list 
print(book.items())

# 4. setdefault- We can add single key and its value and it returns added key's value.
# It key already exist then it returns its value.But does not modify its value.
book.setdefault("CSS",799)
print(book) 

# 5. update-Using it we can add multile keys and its values.And we can also modify existing keys and its values 
book.update({"Python": 550, "ML":1010})
print(book)

# 6. get()-It returns the given key's value.
# If key does not exist it does not return anything if any message is not there.
print(book.get("Python"))
