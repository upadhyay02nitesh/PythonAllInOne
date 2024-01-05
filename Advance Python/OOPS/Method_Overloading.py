#Python not support method overloading functionality in 
# overloading we can wriiten same method that ca perform more than one task

class Cal:

    def product(self,a, b):
        p = a * b
        print(p)


    def product(self,a, b, c):
        p = a * b*c
        print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
c=Cal()
c.product(4, 5, 5)


