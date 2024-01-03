print("Arithmatic operator")
a=50
b=20
print(a+b,a-b,a*b,a/b,a//b,a**b)

print("Relational operator")
print(a<b,a>b,a==b,a<=b,a>=b)

print("Logical Operator")
a=0
b=1
c=1
d=0
print(a and b,b and c,a and c,a and d)
print(a or b,a or c, b or d,a or d,b or c)

print(not a,not b,not c,not d)

a=10
b=20
c=100
d=500
print(a<b and c)
print(a>b and c and d)

print("Assignment operator")
a=10
a+=10
a-=5
print(a)

print("Bitwise operator")
a=10
b=8
print(a & b,a | b,a ^ b,~a,~b)   
print(a<<b) 
print(a>>b)                

print("Membership Operator")

a="hi kalu ashwani kaha ha"
print("hi" in a)
print("hi" not in a)

print("identity Operator")
a=10
b=2
c=10
print(id(a),id(b),id(c))
print(a is b,b is c,a is c)
print(a is not c)


print("operator precedence")
a=(1+1)*2**4//3+4-1
#   (2   *   16/3+3)
print(a)


