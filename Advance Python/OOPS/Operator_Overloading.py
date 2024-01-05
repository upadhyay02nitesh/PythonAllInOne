#When operator perform more than what actual doing 

print("use of + operator for adding",10+20)

print()

print("Add Two Class object using plus + operator")

class A:
    def __init__(self,x):
        self.x=x 
    def __add__(self,other):
        return self.x+other.x

class B:
    def __init__(self,x):
        self.x=x 

a=A(100)
b=B(200)
print(a+b)