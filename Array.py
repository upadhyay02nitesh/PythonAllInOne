# !-D Array
from array import*
a=array('i',[1,2,3,4,5])
print(a,type(a))
for i in a:
    print(i,end=" ")
for i in range(len(a)):
    print(i,a[i],end=" ")

# Function Of Array
a.append(6)
print(a)

a.pop()
print(a)

a.pop(0)
print(a)

a.remove(2)
print(a)

print(a.index(3))

a.reverse()
print(a)

s=array('i',[9,8,7])
a.extend(s)
print(a)

a.insert(0,100)
print(a)

# n=int(input("Enter the number of element"))
# p=array('i',[])
# for i in range(n):
#     p.append(int(input("Enter Element")))
# print(p)


# Slicing

d=array('i',[11,22,33,44,55])
print(d[2:4])

print(d[-1])
print(d[-5:-3])
print(d[::-1])
print(d[0:5:2])



