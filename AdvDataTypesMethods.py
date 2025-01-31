'''
Iterable objects:
List
tuple
strings
range
dict-list of keys will be created
set
# list method always accept iterable objects
# tuple method always accept iterable objects
'''
# l1 = list(5)
# print(l1)#int is not iterable

li1 = list('HARSHI')
print(li1) #['H','A','R','S','H','I']

li2 = list((10,20))
print(li2) #[10,20]

li3 = list({100,200})
print(li3) #[200,100]

li4 = list({'Name':'priya','age':22})
print(li4) #['Name', 'age]

li5 = list(range(1,11))
print(li5)