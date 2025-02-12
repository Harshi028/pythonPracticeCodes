# def disp(a,b):
#     # print(a/c) #nameError
#     print(a/b)
# # disp(10,20)
# disp(10,'kodnest')  #typeError

def chechAge(age):
    if age<18:
        raise ValueError('Age must be greater than 18') #we raised built in exception
try:
    chechAge(12)
except ValueError as e:
    print('Error message:',e)

    