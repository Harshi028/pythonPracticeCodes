'''
1.in tuple we can store homogeneous and heterogeneous type of data
2.in tuple we can store duplicate values.
3.tuple is ordered collection of data:order of insertion will remain as it is in the output
4.tuple are immutable : once we create the list we cannot modify

'''
# tup1 = (10,22.55,'harshi',True,10)
# print(tup1)

# tup1.append(40) #error
# tup1.remove(55) #error
# tup1.pop() #error
# del tup1 #delete the complete tuple

# concatination
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2
print(t3)

# create a singleton tuple:
tup = (10,) #if single value is there we should give , there
print(tup,type(tup))

new_tuple = (10,20,30,40)
# ele1 = new_tuple[0]
# ele2 = new_tuple[1]
# unpacking the tuple
ele1,ele2,ele3,ele4 = new_tuple
print(ele3)
