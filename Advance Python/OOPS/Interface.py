# in python no interface feature are there but using abstract class we can find this feature 
# we can use only abstract mmethod without any concreate method.

from abc import ABC,abstractmethod
class Main(ABC):

    @abstractmethod
    def method1(self):
        pass 
    
    @abstractmethod
    def method2(self):
        pass 

class SubMain(Main):
    def method1(self):
        print("i am method 1")

class SubsubMain(SubMain):
    def method2(self):
        print("i am method 2")       
    
    
s=SubsubMain()
s.method1()
s.method2()