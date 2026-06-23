class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implenent this abstract class")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof"


class Cat(Animal):
    def speak(self):
        return self.name + " says meow"


fido = Dog("Fido")
tom = Cat("Tom")

for pet in [fido, tom]:
    print(pet.speak())