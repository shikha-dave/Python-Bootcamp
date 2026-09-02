class Animal():
    def __init__(self):
        print("Animal created") 


    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating") 


class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self)
        self.name = name
        print("Dog created")

    def who_am_i(self):
        print("I am a dog")

    def speak(self):
        print(f"{self.name} says Woof Woof")

class Cat():
    def __init__(self, name):
        self.name = name
        print("Cat created")

    def who_am_i(self):
        print("I am a cat")

    def speak(self):
        print(f"{self.name} says Meow Meow")


my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

my_dog.who_am_i() # inheritance 

my_dog.speak() # polymorphism


my_cat.speak() # polymorphism


for pet in [my_dog, my_cat]:
    print(type(pet))
    pet.speak() # polymorphism

def pet_speak(pet):
    pet.speak()

pet_speak(my_dog)
pet_speak(my_cat)