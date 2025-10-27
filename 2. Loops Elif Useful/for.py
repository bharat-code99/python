# for num in range(10):
#     print(num + 1)

# for num in range(20):
#     if num % 2 != 0:
#         print(num + 1)

# count = 0
# for alpha in "Python Programming":
#     if alpha == 'o':
#         count += 1
# print(count)

# my_list = ["red", "blue", "yellow"]
# for color in my_list:
#     print(color)

# numbers = [3, 5, 7, 2, 8]
# sum = 0
# for num in numbers:
#     sum += num
# print(sum)

# num = int(input("Enter a num: "))
# for i in range(10):
#     print(num * (i + 1))

# matrix = [[1, 2], [3,4], [5, 6]]
# for row in matrix:
#     for num in row:
#         print(num)

# num = int(input("Enter a number: "))
# for i in range(1, num+1):
#     for j in range(i):
#         print("*", end="")
#     print()

for num in range(2, 51):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)