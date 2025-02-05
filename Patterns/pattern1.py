# n=5
# print('*'*n)

rows = 5
col = 5
# for i in range(rows):
#     for j in range(col):
#         print('*',end='')
#     print() 

# right angled triangle
# for i in range(rows):
#     for j in range(i+1):#(i,rows)
#         print('*',end = ' ')
#     print()

# for i in range(rows):
#     for j in range(col-i):
#         print('*',end=' ')
#     print()

# combination if increasing and decreasing pattern-right pascel triangle
# for i in range(rows):
#     for j in range(i+1):#(i,rows)
#         print('*',end = ' ')
#     print()

# for i in range(rows):
#     for j in range(col-i-1):#(i,rows-1)
#         print('*',end=' ')
#     print()


# decreasing (i,rows)
# increasing (i+1)
# for i in range(rows):
#     for j in range(i+1):
#         print('*',end=' ')
#     for j in range(i,rows-1):
#         print(' ',end=' ')
#     for j in range(i,rows-1):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()
# for i in range(rows):
#     for j in range(i,rows-1):
#         print('*',end=' ')
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(i,rows-1):
#         print('*',end=' ')
#     print()

# diamond
for i in range(rows):
    for j in range(i,rows):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    for j in range(i,rows):
        print(' ',end=' ')
    print()
for i in range(rows):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,rows):
        print('*',end=' ')
    for j in range(i,rows-1):
        print('*',end=' ')
    for j in range(i+1):
        print(' ',end=' ')
    print()