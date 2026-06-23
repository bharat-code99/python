class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am animal")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def who_am_i(self):
        print("I am dog")


my_animal = Animal()
my_animal.who_am_i()
my_dog = Dog()
my_dog.who_am_i()