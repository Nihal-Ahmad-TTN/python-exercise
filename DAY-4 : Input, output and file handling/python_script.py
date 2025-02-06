import os
from abc import xyz
class DummyClass:
    dummy_variable, z = "This is a class variable", "sccd"

    def __init__(self,name):
        self.name = name

    def display_message(self):
        print(f"Hello, {self.name}!")
        print(f"Class Variable: {DummyClass.dummy_variable}")

if __name__ == "__main__":
    obj = DummyClass("Alice")
    obj.display_message()