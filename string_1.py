s="hi how are you"
print(type(s))

s1="""hi how are
    you man
    how is it going"""

print(type(s))

for i in range(len(s)):
    print(i,s[i],end=" ")

print(s*2)

print("Codeshop"+"By"+"Nitesh")

a="Code"
b="Code"
print(a==b)

#Formating of String
#C-Style
print("%d %s"% (432,"kalu"))

#Format Method
print("{}".format(10))

name="Kalu"
age=2
print("My Name is {} And My Age Is {}".format(name,age))

#F-String
print(f"My Name is {name} And My Age Is {age}")

#String Function

s="Codeshop By Nitesh9"
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.isupper())
print(s.islower())
print(s.istitle())
print(s.isdigit())
print(s.isalpha())
print(s.isalnum())
print(s.isspace())
print(s.lstrip())
print(s.rstrip())
print(s.strip())

print(s.replace("Code","Decode"))
print(s.split(" "))

s=s.split(" ")
l='-'.join(s)
print(l)

print(l.startswith("Code"))
print(l.endswith("sh9"))

s="Code By"
print(s.replace(" ",""))

