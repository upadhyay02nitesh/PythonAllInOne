# we are changing main function without interfare the main function

def decor(main):
    def inner():
        a=main()
        add=a+10
        return add 
    return inner

@decor  #it will executed 10+10=20
#MAin Function
def main():
    return 10

print(main())




#Another examole with two decorator

def decor(main):
    def inner():
        a=main()
        multi=a*10
        return multi
    return inner 

def decor1(main):
    def inner():
        a=main()
        multi=a+10
        return multi
    return inner

@decor  #after that this one executed 20*10=200
@decor1  #it will executed first 10+10=20

# #MAin Function
def main():
    return 10

print(main())

