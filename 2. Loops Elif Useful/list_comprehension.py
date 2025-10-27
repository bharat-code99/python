# str = 'Hello World'
# list1 = [x for x in str]
# print(list1)

# list2 = [num ** 2 for num in range(1, 11)]
# print(list2)

# list3 = [x ** 2 for x in range(1, 11) if x % 2 == 0]
# print(list3)

# celcius = [22, 27, 30, 36]
# list4 = [((9/5) * temp + 32) for temp in celcius]
# print(list4)

# list5 = [x if x % 2 == 0 else 'Odd' for x in range(1, 11)]
# print(list5)

list6 = [x*y for x in [2,3,4] for y in [1, 10, 100]]
print(list6)