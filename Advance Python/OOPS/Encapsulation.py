print("""Public Member: Accessible anywhere from otside oclass.
Private Member: Accessible within the class
Protected Member: Accessible within the class and its sub-classes""")

print("Public Member")

class A:
    def __init__(self):
        self.a=10
    def public_method1(self):
        print("Public Method value is ",self.a)

class B(A):
   
    def public_method2(self):
        print("Public Method value is ",self.a)

# a=A()
# a.public_method1()
b=B()
b.public_method1()
b.public_method2()
print("Access from outside obj",b.a)


print()
print("Protected Member")

class A:
    def __init__(self):
        self._a=10
    def public_method1(self):
        print("Public Method value is ",self._a)

class B(A):
   
    def public_method2(self):
        print("Public Method value is ",self._a)

# a=A()
# a.public_method1()
b=B()
b.public_method1()
b.public_method2()
print(b._a)

print()
print("Private Member")

class A:
    def __init__(self):
        self.__a=10
    def public_method1(self):
        print("Public Method value is a",self.__a)

class B(A):
   
    def public_method2(self):
        print("Public Method value is ",self.__a)

# a=A()
# a.public_method1()
b=A()
b.public_method1()
# b.public_method2()
# print(b.__a)      

# b=B()
# b.public_method1()
# b.public_method2()
# print(b.__a)