'''
1.in set we can store homogeneous and heterogeneous type of data
2.in set we cannot store duplicate values.
3.set is Unordered collection of data:order of insertion will remain as it is in the output
4.sets are mutable : once we create the list we can modify
5.set doesn't support index type of data
'''

s1 = {10,True,'Harshi',10,20,55.44}
print(s1,type(s1))
# print(s1[0]) #error
s1.add(500)
print(s1)

