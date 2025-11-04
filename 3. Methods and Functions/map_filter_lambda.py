def square(num):
    return num**2

mynum = [1,2,3,4,5,6]

''' 
What map did is it took each item from the list passed it to the given function
the function returned the value after some performing some operation
then the list function created a list of returned values
'''
# print(list(map(square, mynum))) #[1, 4, 9, 16, 25, 36]

def is_even(num):
    return num % 2 == 0

# What filter did is similar to map but in this it kept the items on which the function returned True
# It is important to pass the function that should return either True or False
# print(list(filter(is_even, mynum))) #[2, 4, 6]

# Lamda functions are the shorthand of normal functions
# they do not require prior definition or name
names = ["Andy", "Eve", "Sally"]

# In this example we passed a lambda function
# it returns what is after the ':' colons
print(list(map(lambda name: name[0], names))) #['A', 'E', 'S']