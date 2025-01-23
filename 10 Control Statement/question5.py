#  WAP to calculate electricity bill 

units = int(input("Enter the units consumption : "))

if units<=200:
    print("No Bill")
elif units>200 and units<=400:
    bill=(units-200)*2
    print("Your Bill is : ",bill)
elif units>400 and units<=800:
    bill=(units-200)*4
    print("Your Bill is : ", bill)
elif units>800:
    bill=(units-200)*8+1200
    print("Your Bill is : ", bill)
else:
    print("Please Enter valid Units")