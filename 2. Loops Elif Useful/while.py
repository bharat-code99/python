# num = 1
# while num <= 10:
#     print(num)
#     num += 1

# num = 2
# while num <= 20:
#     print(num)
#     num += 2

# num = int(input("Enter a number: "))
# while num != 0:
#     num = int(input("Enter a number: "))
# else:
#     print("Loop Ended")

# mylist = [1, 2, 3, 4, 5]
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i += 1

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     print(i, end='')
#     i += 1

# num = int(input("Enter a number: "))
# i = 1
# while i <= num:
#     j = 1
#     while j <= i:
#         print('*', end='')
#         j += 1
#     print()
#     i += 1

# num = int(input("Enter a number: "))
# fact = 1
# i = 1
# while i <= num:
#     fact *= i
#     i += 1
# else:
#     print(fact)

# num = int(input("Enter a number: "))
# while num > 0:
#     print(num%10, end='')
#     num = int(num / 10)

# num = int(input("Enter a number: "))
# is_prime = True
# while is_prime:
#     i = 2
#     while i < (int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#         i += 1
#     break
# if is_prime:
#     print(f"{num} is Prime")
# else:
#     print(f"{num} is not Prime")

str = input("Enter a string: ")
count = 0
i = 0
while i < len(str):
    if str[i].isdigit():
        count += 1
    i += 1
else:
    print(f"there are {count} digits in {str}")

# i = 1
# while i < 5:
#     i += 1
#     pass
# else:
#     print("Empty while loop")