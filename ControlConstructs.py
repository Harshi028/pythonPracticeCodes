# linear is default flow of execution
'''
1.conditional : if-else, if-elif
2.looping : for, while
3.jumping : break, continue, pass
'''
def chechAge(age):
    if(age>18):
        print('Age is greater than 18')
    else:
        print('Age is not greater than 18')
chechAge(18)

# wap to display 'Child' if age is in below 18,display 'Adult' age is above 18
# display senior Citizen if age is above 65

def dspAge(agee):
    if(agee<18):
        print("Child")
    elif(agee>18 and agee<65):
        print("Adult")
    elif(agee>65):
        print("Senior citizen")
    else:
        print("invalid")
dspAge(int(input('Enter age')))