# __init__ --dunder menthod -- dunder means double underscore,magic method
# __add__

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def work(self):
        print(self.name ,'is working')
e1 = Employee('harshitha',23) #calling of constructor
e1.work()