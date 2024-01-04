#Duck Typing - if it walks like duck and talks like duck then it must be duck

class Duck:
    def Walk(self):
        print("I can walk like duck")

class Horse:
    def Walk(self):
        print("I can walk like Horse")

def myfun(obj):
    obj.Walk()
d=Duck()
myfun(d)

h=Horse()
myfun(h)

#Strong Typing if method are there then executed otherwise not giving error


print()

class Duck:
    def Walk(self):
        print("I can walk like duck")

class Horse:
    def Walk(self):
        print("I can walk like Horse")

def myfun(obj):
    if hasattr(obj,'Walk'):
        obj.Walk()
    else:
        print("This method is not presented")
d=Duck()
myfun(d)

h=Horse()
myfun(h)