# Abstraction = Derived from ABC class which belongs to abc module.
# two methods are there = Abstract Method , Concrete Method

from abc import ABC,abstractmethod

class Defence(ABC):
    @abstractmethod
    def area(self):
        pass 
    #Concreate method

    def gun(self):
        print("AK47")

class Army(Defence):
    def area(self):
        print("Land")

class Airforce(Defence):
    def area(self):
        print("SKY")

class Navy(Defence):
    def area(self):
        print("Water")

n=Navy()
n.area()
n.gun()

print()

a=Airforce()
n.area()
n.gun()

print()

a=Army()
n.area()
n.gun()

