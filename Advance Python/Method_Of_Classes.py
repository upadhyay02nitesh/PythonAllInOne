class AllMethod:

    class_variable="classes"
    def __init__(self):
        self.a=10
    
    #Instance Method
    
    def instance_method(self):
        print("Instance method ",self.a)
    
    #Class Method
    
    @classmethod

    def class_method(cls):
        print(cls.class_variable)

    #Static Method
    @staticmethod

    def static_method():
        print("I am static method")

a=AllMethod()
a.class_method()
a.instance_method()
a.static_method()

print()

AllMethod.class_method()
AllMethod.static_method()
# AllMethod.instance_method()


print("Accessor Method - Access or Read data")
class AllMethod:

    class_variable="classes"
    def __init__(self):
        self.a=10
    
    #Instance Method
    
    def instance_method(self):
        return self.a 
a=AllMethod()
print(a.instance_method())

print("Mutator Method -Read and modify the data ")

class AllMethod:

    class_variable="classes"
    def __init__(self):
        self.a=10
    
    #Instance Method
    
    def instance_method(self):
        self.a=60 
al=AllMethod()
#Before Modify
print(al.a)

#After Setting
al.instance_method()
print(al.a)