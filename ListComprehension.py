# square of list from list
li1 = [1,2,3,4,5]
# sq_list = []
# for i in li1:
#     sq_list.append(i**2)
# print(sq_list,end=' ')

'''
List comprehension:
syntax: [expression to return for i in iterable_object condition]
new_list = [i for i in li1]
sq_list = [i**2 for i in li1]
'''
duplicate_li1 = [i for i in li1]
even = [i for i in li1 if i%2==0]
sq_list = [i**2 for i in li1]
new_list = [ele+2 for ele in li1]
print(duplicate_li1)
print(even)
print(sq_list)
print(new_list)