d={}
print(type(d))

d={1:'mohan',2:'sohan'}
for i in d:
    print('Key',i,"Value",d[i])

d[3]='rohan'
print(d)

del(d[2])
print(d)

#Testing key 
print(3 in d)

di=d.copy()
print(di)
print(id(di),id(di))

#get value access
for i in d:
    print(d.get(i))

itm=d.items()
print(itm)

key=d.keys()
print(key)

value=d.values()
print(value)

#Add multiple element
d.update({4:'koyal',5:'chhote'})
print(d)

for key,value in d.items():
    print(key,value)

#specific element
d.pop(5)
print(d)

#remove last element
d.popitem()
print(d)

#if same element not founded then inserted

d.setdefault(6,'kalu')
print(d)

#this will not executed because its already are there
d.setdefault(6,'kalu')
print(d)

# dict={}
# n=int(input("Enter the how many element you can want to inserted "))
# for i in range(n):
#     k=input("Enter the Key ")
#     v=input("Enter the Value ")
#     dict.update({k:v})
# print(dict)

#Nested Dictionay

nestd={'Rama':'Seeta',"Ram":'Lakshaman',1:{'Hanuman':'JaiShreeRam'}}
# print(nestd[1])
# print(nestd[1]['Hanuman'])

for i in nestd:
    if type(nestd[i]) is dict:
        for j in nestd[i]:
            print(j,":",nestd[i][j])
    else:
        print(i,":",nestd[i])