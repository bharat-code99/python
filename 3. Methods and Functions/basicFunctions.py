
# def super_employee(emp_list):
#     max_hour = 0
#     emp_name = ''
#     for name, hour in emp_list:
#         if hour > max_hour:
#             max_hour = hour
#             emp_name = name
#     return emp_name, max_hour
#
# if __name__ == "__main__":
#     work_hours = [("Bharat", 100), ("Rahul", 150), ("Priti", 250), ("Anshu", 300)]
#     emp_of_month = super_employee(work_hours)
#     name, hours = super_employee(work_hours)
#     print(emp_of_month)

# def add(a = 0, b = 0):
#     return a+b
#
# print(add(9, 10))

# def greet(name = "Guest"):
#     print(f"Hello {name}!")
#
# greet("Anshu")

# def is_even(num):
#     return num % 2 == 0
#
# result = is_even(9)
# print(result)

# def factorial(num):
#     fact = 1
#     for i in range(2, num+1):
#         fact *= i
#     return fact
#
# result = factorial(7)
# print(result)

# def count_vowels(s):
#     vowels = set('aeiouAEIOU')
#     return sum(1 for char in s if char in vowels)
#
# print(count_vowels("hello"))

def my_func(word):
    return ''.join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(word)
    )

print(my_func('Anthropomorphism'))