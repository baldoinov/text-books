# This code was produced through the reading of this tutorial: https://realpython.com/python3-object-oriented-programming/

class Dog:
    
    species = "Canis Familiaris"

    def __init__(self, name, age, breed) -> None:
        
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class JackRussellTerrier(Dog):
    
    def speak(self, sound="Arf"):
        return super().speak(sound)

class GoldenRetriever(Dog):
    
    def speak(self, sound="Bark"):
        return super().speak(sound)


class Car:

    def __init__(self, color: str, mileage: int) -> None:
        
        self.color = color
        self.mileage = mileage
    
    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage:,} miles"

if __name__ == '__main__':

    blue = Car("blue", 20000)
    red = Car("red", 30000)

    print(blue)
    print(red)
