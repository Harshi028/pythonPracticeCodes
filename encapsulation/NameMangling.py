class Demo1:
    def __init__(self,name):
        self.__name = name   #Private Variable

d1 = Demo1('Aksah')
# print(d1.__name) error
print(d1._Demo1__name)
'''
1.NameMangling is the process of providing newName to the private variables
2.these new names will be provided automativally by python for all private members.
3.NewName will be provided in the format: _className__variable name 

'''