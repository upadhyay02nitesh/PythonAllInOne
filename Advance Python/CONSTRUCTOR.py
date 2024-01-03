#Without Parameter
class Const:
    def __init__(self):
        print("Constructor - The special Method Naam to suna hoga")
c= Const()

#With Parameter

class Constr:
    def __init__(self,a):
        self.a=a 
        print("Passing the argument")

c=Constr(10)
print(c.a)

#prefrence

class Constr:
    def __init__(self,a=11):
        self.a=a 
        print("Passing the argument")

c=Constr(10)
print(c.a)