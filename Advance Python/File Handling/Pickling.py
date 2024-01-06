print("Pickling is a process to convert class object into bytestream and can store into the file")
# dump() function is used for Pickling

# import pickle
# class Student:
#     def __init__(self,name,roll):
#         self.name = name 
#         self.roll = roll 
#     def meth1(self):
#         print(f'Name :{self.name} Roll:{self.roll}')

# with open('stu.dat',mode='wb') as f:
#     s=Student("kalu",101)
#     pickle.dump(s,f)
#     print("Pickling Done")

print("Unpickling - convert  byte stream into class object load() for ")

import pickle

class Student:
    def __init__(self,name,roll):
        self.name = name 
        self.roll = roll 
    def meth1(self):
        print(f'Name :{self.name} Roll:{self.roll}')

with open("stu.dat",mode='rb') as f:
    obj=pickle.load(f)
    obj.meth1()
    print("Unpickling Done !!!")
