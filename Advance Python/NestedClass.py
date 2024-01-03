class Outer_Class:
    def __init__(self):
        self.a=10
    
    #Instance Method
    
    def instance_method1(self):
        print("Instance method Outer ",self.a)

    class Inner_Class:
        def __init__(self):
            self.a=50
    
        #Instance Method
        
        def instance_method2(self):
            print("Instance method Inner ",self.a)

a=Outer_Class()
a.instance_method1()

#Calling inner
b=Outer_Class().Inner_Class()
b.instance_method2()
