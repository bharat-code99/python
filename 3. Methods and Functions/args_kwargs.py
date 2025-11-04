# def myfunc(*args):
#     return sum(args)
#
# print(myfunc(1, 2, 3, 4, 5))

# def myfunc(*args):
#     for item in enumerate(args):
#         print(item)
#
# myfunc('a', 'b', 'c', 'd')

def myfunc(**kwargs):
    print(kwargs)
    if 'name' in kwargs:
        print(f"My Name is {kwargs['name']}")
    else:
        print("Please pass a name.")
    if 'age' in kwargs:
        print(f"I am {kwargs['age']} years old.")
    else:
        print("Please pass your age.")
    if 'job' in kwargs:
        print(f"I work as a {kwargs['job']}")
    else:
        print("Please pass your job title.")

myfunc(name='Bharat', age=24, job='Developer')