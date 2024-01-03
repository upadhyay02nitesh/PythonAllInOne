#Inheritance -Inheri the property of parent class

print("Single Inheritance - Class Derived from  Base Class")

class Parent:

    class_variable="yes"
    def __init__(self):
        print("Parent Class Constructor ")
        self.a=10
    def method1(self):
        print(self.a)
    
    @classmethod

    def class_method(cls):
        print(cls.class_variable)

    #Static Method
    @staticmethod

    def static_method():
        print("I am static method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class Constructor ")
    def method2(self):
        print("Child Method")
    
c=Child()
c.method1()
c.class_method()
c.static_method()

print() 
print('Another Example')


class Parent:
    class_variable = "yes"

    def __init__(self, c, d):
        print("Parent Class Constructor ")
        self.a = 10
        self.c = c
        self.d = d

    def method1(self, e, f):
        print("Parent Method1:", self.a, self.c, self.d, e, f)

    @classmethod
    def class_method(cls):
        print("Class Method:", cls.class_variable)

    @staticmethod
    def static_method():
        print("Static Method")

class Child(Parent):
    def __init__(self, c, d):
        self.a = 30  # This value overrides in the parent class
        self.b = 90
        super().__init__(c, d)
        print("Child Class Constructor ")

    def method2(self):
        print("Child Method2:", self.a, self.b, self.c, self.d)

c = Child(11, 22)
c.method1(60, 70)
c.class_method()
c.static_method()
print(c.a)
c.method2()

print()

print("Multilevel inhertance - class derived more than one parent class")


class Parent:

    class_variable="yes"
    def __init__(self):
        print("Parent Class Constructor ")
        self.a=10
    def method1(self):
        print("Parent Method",self.a)
    

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Class Constructor ")
    def method2(self):
        print("Child Method")

class GrandChild(Child):
    def __init__(self):
        super().__init__()
        print("GrandChild Class Constructor ")
    def method3(self):
        print("GrandChild Method")


     
g=GrandChild()
g.method1()
g.method2()
g.method3()

print()
print("Hierachical Inheritance - inherit more than one child class using same parent class")


class Parent:
    class_variable="yes"
    def __init__(self):
        print("Parent Class Constructor ")
        self.a=10
    def method1(self):
        print("Parent Method",self.a)
    

class Child1(Parent):
    def __init__(self):
        super().__init__()
        print("Child1 Class Constructor ")
    def method2(self):
        print("Child1 Method")

class Child2(Parent):
    def __init__(self):
        super().__init__()
        print("Child2 Class Constructor ")
    def method3(self):
        print("Child2 Method")


     
g=Child1()
g.method1()
g.method2()

g=Child2()
g.method1()
g.method3()

print()
print("Multiple Inheritance - inherit chile class more than one parent class")

class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor ")
        self.a=10
    def method1(self):
        print("Father Method",self.a)
    

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class Constructor ")
    def method2(self):
        print("Mother Method")

class Child(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Child Class Constructor ")
    def method3(self):
        print("Child Method")


     
g=Child()
g.method1()
g.method2()
g.method3()

