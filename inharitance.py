# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"  # Override the speak method

# Creating an instance of Dog
dog = Dog("Buddy")
print(dog.speak())  


class Cat(Animal):
    def __init__(self, name):
        self.sound = "meows !!!"
        super().__init__(name)
    def speak(self):
        return f"{self.name} {self.sound}"  

cat = Cat("COCO")
print(cat.speak())


class Robot(Animal):
    def is_animal(self):
        return f"{False} -----> {self.name}"
    
robot =Robot("ALEX")
print(robot.is_animal())
