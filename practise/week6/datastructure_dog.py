class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def say(self, sound):
        print(f"{self.name} says {sound}")

    def eat(self, food):
        print(f"{self.name} eats {food}")


if __name__ == "__main__":
    new_dog = Dog('Hachiko', 5)
    new_dog.description()
    new_dog.say('Hello')
    new_dog.eat('bone')
