a=set()
print(type(a))

a={'hello',12,2.0,2+3j}
print(a)

for i in a:
    print(i)

#Add one element
a.add('python')
print(a)

#Add multiple element

a.update(['hao',1,2])
print(a)

a.remove('hao')
print(a)

a.discard('python')
print(a)

# s=set()
# n=int(input("Enter how many The Element --:"))
# for i in range(n):
#     s.add(input("Enter the element ---:"))
# print(s)


b=a.copy()
print(b)
print(id(a),id(b))

set1={1,2,3,4,5}
set2={2,3,4,5,6}
intr=set1.intersection(set2)
print(intr)

uni=set1.union(set2)
print(uni)

diff=set1.difference(set2)
print(diff)

diff=set2.difference(set1)
print(diff)

isb=set1.issubset(set2)
print(isb)

isp=set1.issuperset(set2)
print(isp)

#set does not contain duplicate value
set3={1,2,3,1,2,3,4,5,6,7}
print(set3)