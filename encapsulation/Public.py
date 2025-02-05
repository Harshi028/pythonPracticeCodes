'''
1.public--public itself is a default in python
RULE: It should be access inside the class, outside the class
2.Protected-->>_variable
RULE: it shoulb be access inside the same class in which we have declared and inside child class 
3.Private-->>__variable
RULE: it shoulb be access inside the same class in which we have declared

4.access modifiers/specifiers: to determine the accebility of data menmbers and member functions
'''

class Demo1:
    def __init__(self,name):
        self.firsname = name
    def disp1(self):
        print(self.firsname)
d1=Demo1('akash')
print(d1.firsname)
d1.disp1()
class Demo2(Demo1):
    def disp2(self):
        print(self.firsname)
d2=Demo2('pooja')
print(d2.firsname)
d2.disp2()
