# debugging- way of testing a unit - the smallest peace of code /finding and fixing the bug
# from program

# pdb module in python is used for debugger

import pdb 
def sum(a,b):
    print(a+b)

def multi(a,b):
    print(a*b)

pdb.set_trace()
sum(11,2)
multi(11,2)

#here when we trace our code then  we use 'l' for tracking where our cursor point
# 'n' for execute particular position
# 'q' for quit

