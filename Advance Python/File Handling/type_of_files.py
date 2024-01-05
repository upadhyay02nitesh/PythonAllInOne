# Files == it is a data that is available for program
# types -text, binary
# text - that contain char and string form
# binary- in the form of bytes and use for img video pdf etc file

print("Create file in Python writing data in Python")

f=open("file1.txt",mode='w')
f.write("hello this is the first file using text format")
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


