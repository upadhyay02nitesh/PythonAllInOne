#Child method override parent method

class Main:
    def sum(self,a,b):
        print("parent method ",a+b)

class Submain(Main):
    def sum(self,a,b):
        print("Second method",a*b)

s=Submain()
s.sum(10,20)

print()
#For call Parent method use super method

class Main:
    def sum(self,a,b):
        print("parent method ",a+b)

class Submain(Main):
    def sum(self,a,b):
        super().sum(a,b)
        print("Second method",a*b)

s=Submain()
s.sum(10,20)