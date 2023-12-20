#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

# Example usage:
fido = Dog("Fido", "Labrador")
print(fido.name)   # Output: Fido
print(fido.breed)  # Output: Labrador
fido.bark()        # Output: Woof!
