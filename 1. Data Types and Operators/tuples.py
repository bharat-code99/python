tup = ("One", 2, 3.0, [4, 5], 4, 5, 2)
# tup[0] = 1  #TypeError: 'tuple' object does not support item assignment
tup[3][1] = 6

# print(tup.count(4))  # 1
print(tup.index(2))  # 1