#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} says: Hello World!")

    def walk(self):
        print(f"{self.name} is walking.")

# Example usage:
john = Person("John")
print(john.name)   # Output: John
john.talk()        # Output: John says: Hello World!
john.walk()        # Output: John is walking.
