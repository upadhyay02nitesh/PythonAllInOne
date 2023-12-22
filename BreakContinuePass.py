#Break Statement
for i in range(10):
    if i==3:
        break
    print(i)

print()
#Continue Statement
for i in range(5):
    if i==3:
        continue
    print(i)

print()
#Pass Statement
for i in range(5):
    pass
    for i in range(2):
        print("Inner",i)
else:
    print("Done")
        