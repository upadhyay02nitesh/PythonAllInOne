#List Comprehesion

#Normal Process
l=[]
for i in range(3):
    l.append(i)
print(l)

#Comprehension
l=[i for i in range(3)]
print(l)

#If else
l=[i for i in range(1,11) if i%2==0 if i%5==0 ]
print(l)

l=[i if i%2==0 else "Invalid" for i in range(1,11)]
print(l)

#Nested list comprehension
l=[[i*j for j in range(1,11)] for i in range(2,3)]
print(l)


print(("Set Comprehension"))
#Normal Process
s=set()
for i in range(2):
    s.add(i)
print(s)

#Comprehension

s={i for i in range(2)}
print(s)

s={i for i in range(10) if i%2==0}
print(s)


s={i if i%2==0 else "Invalid" for i in range(1,11)}
print(s)

#it returns only one invalid because it does not contain any duplicate value Right !

print("Dict Comprehension")

#Normal processs
d={}
for i in range(3):
    d.update({i:i*2})
print(d)

#Comprehension
d={i:i*2 for i in range(10)}
print(d)

d={i:i*2 if i%2==0 else "Invalid" for i in range(10)}
print(d)
