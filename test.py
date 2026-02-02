x = 2
y = 2
z = 2
n = 2
my_list = [[a,b,c] for a in range(x) for b in range(y) for c in range(z) if a+b+c != n]
print(my_list)

# new_list = list(zip(list(range(x)), list(range(y)), list(range(z))))
# print(new_list)