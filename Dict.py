'''
1.in Dict we can store homogeneous and heterogeneous type of data
2.in Dict we cannot store duplicate keys,we can store duplicate values
3.Dict is ordered collection of data:order of insertion will remain as it is in the output
4.Dict are mutable : once we create the list we cann modify
'''
# key value pairs
d1 = {'name':'harshi','age':29,'phone':7032510166,'age':300} #{'name': 'harshi', 'age': 300, 'phone': 7032510166}
print(d1,type(d1))
d1['name'] = 'Poojaa'
print(d1)

marks = {'sci':85,'Maths':85}
print(marks)

for i in d1.keys():
    print(i)
print()
for i in d1.values():
    print(i)
print()
for i in d1.items():
    print(i)    # ('name', 'Poojaa')
                # ('age', 300)
                # ('phone', 7032510166)