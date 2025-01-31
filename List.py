'''
1.in list we can store homogeneous and heterogeneous type of data
2.in list we can store duplicate values.
3.list is ordered collection of data:order of insertion will remain as it is in the output
4.list are mutable : once we create the list we can modify
'''
li1 = [10,20,44.6,True,'Harshi',20]
print(li1,type(li1))
li1.append(300)
print(li1)
li1.insert(1,'hiii')
print(li1)
li1.remove(20)
print(li1)

# whether the element is present or not:in and not in operator
print(2000 in li1) #False
print('Harshi' in li1) # True

# pop() will remove the last element from list and return that element
print(li1.pop())

# del keyword : it is a keyword it will not return
# li1.pop(1)--it ia a function it will return deleted element
del li1[1]
print(li1)

del li1 #it will delete complete list
print(li1) #li1 is deleted so we get an error as li1 is not defined



