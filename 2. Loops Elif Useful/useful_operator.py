# word = 'abcde'
# # for item in enumerate(word):
# #     print(item)
# for index, item in enumerate(word):
#     print(f"{index} => {item}")

# list1 = list(range(1, 6))
# list2 = ['a', 'b', 'c']
# # for combined in zip(list1, list2):  # It only combines till the shortest list
# #     print(combined)
# for item1, item2 in zip(list1, list2):
#     print(f"{item1} => {item2}")

# list1 = list(range(1, 11))  # To check if the given item is present in the list, string or dictionary
# print(5 in list1)  # True

# from random import shuffle # Shuffle list in place, and return None.
# my_list = list(range(1, 11))
# shuffle(my_list)
# print(my_list)

from random import randint #Return random integer in range(a, b), including both end points.
num = randint(1,2)
print(num)