class Demo1:
    def disp1(self):
        print("Inside disp1")
        '''
        in py if we print reference variable then internally python 
        will invoke __str__() which always returnd string representation
        of an addresss of an object
        in the below examples we have ovverridden __str__ methods in their
        '''
    def __str__(self): #method overriding
        return 'Hello'
    def __add__(self,other):
        self.a = 20
        other.b = 30
        return self.a + other.b
class Demo2:
    def disp2(self):
        print("Inside disp2")
    def __str__(self):
        return 'Hiii'
d1 = Demo1()
d2 = Demo2()
# in python if we print ref variable then it will display string representation of an adress of an object
print(d1)
# print(d1+d2) -concatination never happend with object
print(d2)

#dundur-methods:---> the methods which has sufix and prefix as __
# also called as magic methods because as programmer we no need to call any methods ,automatically methods will be invoked.
print(d1+d2)