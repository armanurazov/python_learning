# syntax errors are not able to be cought by exception handlers

try:
    print(10 + '10') #TypeError
except:                   
    print('types do not match')


# case where the type of error is specified
try:
    print(10 + '10') 
except TypeError:                   
    print('data types do not match')
finally:
    print('this text will occure anyways - Error or No Error')