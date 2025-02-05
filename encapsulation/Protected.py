class Demo1:
    def __init__(self,name):
        self._firsname = name #protected variable
    def disp1(self):
        print(self._firsname)
d1=Demo1('akash')
print(d1._firsname)
d1.disp1()

class Demo2(Demo1):
    def disp2(self):
        print(self._firsname)
d2=Demo2('pooja')
print(d2._firsname)
d2.disp2()

class Demo3:
    def disp3(self):
        print(d1._firsname)
d3=Demo3()
d3.disp3()