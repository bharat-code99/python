x = 50
def func(x):
    print(f"X is {x}")

    x = 'New Value'
    print(f"I just locally changed the X to {x}")
    return x

x = func(x)
print(f"X is {x}")
