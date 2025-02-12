def disp(a,b):
    try:
        print('Task started')
        print(a/b)
    except:
        print('exception occur')
    else:
        print('task excecuted without any exception')
    finally:
        print('task ended')
    print('---------------------------')
disp(10,0)
disp(10,5)
disp(20,2)

'''
try: used to keep the logic in which we may get some error 
except: will be executed when exception occures in try block logic
else: will executed when try block logic executed without any error
finally: will always executed irrespective of exception occured or not
'''