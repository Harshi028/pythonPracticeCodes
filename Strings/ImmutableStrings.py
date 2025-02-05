''' once we declare the string we can't modify it if we try to modify the string it will create new String  ---IMMUTABLE
if new string doesn't have any reference variable then it will be removed
Python Internally uses String Interning.
String Interning is the process of checking string before creating any new object.
whenever we want to create new object, python first intern pool, weather thatobject already exist or not.
when the object already exist in the string intern Records then address of existing object will be reused'''

# s1 = 'KodNest'
# s1 = s1.upper()
# print(s1)

# s1 = 'K'
# print(s1,id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1,id(s1))
print(s2,id(s2))

print(s1[0])
print(s2[-1])

print('Id of H:',id(s1[0]))
print('Id of o:',id(s1[-1]))