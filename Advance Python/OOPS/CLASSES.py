#Classes And Objects
print("Classes   =   Attributes + Methods")


#Creating Class
class OOPS:
    def __init__(self):
        print("Special Method executed when we create class of object")
        self.one="oops_first"  #attribute
    def class_method(self):   #Method
        print(self.one)

#Creating object
o=OOPS()
#Calling the method
o.class_method()


#pass the argument

class OOPSe:
    def __init__(self,a,b):
        self.a=a 
        self.b=b 

    def oops_method(self,c):
        c=c 
        print("sum of a+b+c = ",self.a+self.b+c)
o=OOPSe(4,8)
o.oops_method(6)

#Access Variable outside of the class
print(o.a)
print(o.b)

#Modifying the variable
o.a=10
o.b=20

print("After Modifying ")
o.oops_method(6)