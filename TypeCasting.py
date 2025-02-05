# if string is holding integer then it can be converted into int
a='30'
print(a,type(a))
b=int(a)
print(b,type(b))

# string to integer conversion is not allowed
x='KODNEST'
print(x,type(x))
# y=int(x)
# print(y,type(y))

# p = float(input('Enter float type data'))
# print(p,type(p))

# bool()
q=12
print(q,type(q))
q=bool(q)
print(q,type(q))

'''
1.while converting int to bool for all non zero values we will get true.
2.while converting int to bool for 0 and empty srings we will get false.
'''