#Classes

class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
    
    def talk(self):
        print("Miau")

felix = Cat("ginger", 4)
print(felix.color)
felix.talk()

#Inheritance

class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
class Cat1(Animal):
    def purr(self):
        print("Purrr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("black", 4)
print(fido.color)
fido.bark()

class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()

#Method overloading (Dunders)
class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

first = Vector2d(5, 7)
second = Vector2d(3, 9)
result = first + second
print(result.x)
print(result.y)

class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("hello world!")
print(spam / hello)

class SpecialString1:
    def __init__(self, cont):
        self.cont = cont
    
    def __gt__(self, other):
        for index in range(len(other.cont) +1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)

spam = SpecialString1("spam")
eggs = SpecialString1("eggs")
spam > eggs