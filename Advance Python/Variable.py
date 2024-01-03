#Instance variable - separate copy created for every object and modification not affect on every copy

class InstanceClass:
    def __init__(self,a,b):
        self.a=10  #instance method
        self.b=20
        self.c=40
    def instance_method(self):
        print(self.a,self.b,self.c)

i=InstanceClass(10,20)
i.instance_method()

s=InstanceClass(10,20)
print(s.a)

print()

s.c=50
print(s.c)

print("Not effect on every copy ")

ij=InstanceClass(10,20)
ij.instance_method()


print("Class Variable")

#class Variable - same copy created for every object and modification affect on every copy

class Classes:
    fp="yes"  #class variable
    def __init__(self):
        self.a=10
    def instance_method(self):
        print(self.a)

    @classmethod
    def class_method(cls):
        print(cls.fp)

c=Classes()  #class obj 
c.class_method()
c.instance_method()

print("""we can acces instance and class variable using instance method but 
using class method we can access only class variable not instance variable """)
#Class Method
Classes.class_method()
# Classes.instance_method()

print(Classes.fp)
print()
Classes.fp="No"
print(Classes.fp)
Classes.class_method()




