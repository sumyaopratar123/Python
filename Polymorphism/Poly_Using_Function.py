class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

def animal_sound(animal):
    animal.sound()

animal_sound(Dog())
animal_sound(Cat())