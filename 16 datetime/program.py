# In Python, dat and time are not datatypes of their own, but a module named DataTime in Python can be imported 
# to work with the date as well as time. Python Datetime module comes build into Python, so there is no need to
# install it externally.

from datetime import date

my_birthday = date(1998, 1, 20)
print("Your Date of Birth is : ",my_birthday)


# Getting current date
today = date.today()
print(today)

# to get year, month and day

today = date.today()
print("Current Year : ", today.year)
print("Current Month : ", today.month)
print("Current Day : ", today.day)

