# Files == it is a data that is available for program
# types -text, binary
# text - that contain char and string form
# binary- in the form of bytes and use for img video pdf etc file

print("Create file in Python writing data in Python")

f=open("file1.txt",mode='w')
f.write("""hello this is the first file using text format
how i can help you""")
print(f)
f.close()

f=open("file2.txt",mode='w')
f.write("hello \n")
f.write("hellohii \n")
f.write("hellojjj")
print(f)
f.close()

print("Reading data using text in Python")

f=open("file1.txt",mode='r')
data=f.read()
print(data)
f.close()

print("Reading data using binary in Python")

f=open("file2.txt",mode='rb')
data=f.read()
print(data)
f.close()


print("Text file mode")
# r=open for reading 
# w= open for write and overwrite the data 
# x=file not available then create and write 
# a= append the data in existing file 
# r+=read and write 
# w+=write and read 
# a+append and read


print("Binary file mode")
# rb=open for reading 
# wb= open for write and overwrite the data 
# xb=file not available then create and write 
# ab= append the data in existing file 
# rb+=read and write 
# wb+=write and read 
# ab+append and read

# f=open("one1.txt",mode='x')
# f.write("hi i am x method")
# f.close()

print("file object variable")
print()

f=open("file1.txt",mode='r')
f.close()
print(f.mode)
print(f.readable)
print(f.closed)
print(f.name)

print()
print("Check file exist or not")

import os 
print(os.path.isfile('file1.txt'))

import os 
if os.path.isfile('file1.txt'):
    f=open('file1.txt',mode='r')
    data=f.read()
    print("File Opened ")
    print(data)
    f.close()
else:
    print("file not available")


print()
print("Writelines method")
# store a group of string also store list,tuple,set
# f=open("file1.txt",mode='w')
# l=["Hi","How","Are","You"]
# f.writelines(l)
# f.close()




# print("Reading Method")
# f=open("file1.txt",mode='r')

# d=f.read()
# print(d)

# print("Read specific char from starting")
# d=f.read(7)
# print(d)

# print("Read one line from starting")

# a=f.readline()
# print(a)


# print("Read line by line from starting and return the list")
# a=f.readlines()
# print(a) 

print("Tell and Seek Method")
# tell- for telling current position of file pointer 
# seek decide where you can move your pointer


# f=open("file1.txt",mode='r')
# print(f.tell())
# print(f.read(5))
# print(f.tell())
print("working like range and increase after and after from 0 position ")
# print(f.read(5))
# print(f.tell())

# f.seek(7)
# print(f.tell())

# print("reading from where you can put your pointer not from starting Right ! ")
# f.seek(2)
# print(f.read())
# print(f.tell())


# print("Copy file element to another")
# print("copy file1 element to file2")

# f1=open("file1.txt",mode='r')

# f2=open("file2.txt",mode='w')
# d=f1.read()
# f2.write(d)
# f1.close()
# f2.close()



print("""With Statement- used to not close file every time 
it can close itself after operation""")
print()

with open("file1.txt",mode='r') as f:
    d=f.read()
    print(d)

print(f.closed)




 