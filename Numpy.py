#2-D Array

from numpy import*
# a=array([1,2,3,4,5])
# print(a)

a=array([[1,2,3,4,5],
         [6,7,8,9,10]])
for i in a:
    for j in i:
        print(j,end=" ")
    print()

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

d=a.flatten()
print(d)

a=array([1,2,3,4,5,6])
print(reshape(a,(2,3)))

