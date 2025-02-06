# Write a program to filter all the even numbers from the list using lambda function

num = [12, 33, 41, 44, 25, 99, 1010, 309]

even = filter(lambda x: x % 2 == 0, num)
print(list(even))