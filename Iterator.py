a=("Ba","pa","la")
it=iter(a)
print(next(it))
print(next(it))
print(next(it))

print()

class Iterator:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x 
g=Iterator()
it=iter(g)
print(next(it))
print(next(it))
print(next(it))