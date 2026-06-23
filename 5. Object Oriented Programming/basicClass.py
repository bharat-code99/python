class Dog:
    species = 'mammal'
    def __init__(self, breed:str, name:str, spots:bool, spec:str):
        self.breed = breed
        self.name = name
        self.spots = spots
        self.species = spec

    def bark(self):
        print(f"{self.name} said {'Woof! ' * 3}")


my_dog = Dog("Golden", "Bruno", False, 'fish')
print(f"{my_dog.breed} {my_dog.name} {my_dog.spots} {my_dog.species}")
my_dog.bark()