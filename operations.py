from math import *
from converter import *

def operate(num1, num2, convertType, operation):
    if convertType == 'polar':
        num1 = convert(num1, 'imaginary')
        num2 = convert(num2, 'imaginary')
        newNum = convert(operate(num1, num2, 'imaginary', operation), 'polar')
    elif convertType == 'imaginary':
        if '+' in num1:
                num1List = num1.split('+')
        elif '-' in num1:
            num1List = num1.split('-')
            num1List[1] = '-' + num1List[1]
        if '+' in num2:
                num2List = num2.split('+')
        elif '-' in num2:
            num2List = num2.split('-')
            num2List[1] = '-' + num2List[1]
        
        real1 = num1List[0]
        imaginary1 = num1List[1]
        real2 = num2List[0]
        imaginary2 = num2List[1]
        
        if operation == 'add':
            pass
        elif operation == 'subtract':
            pass
        elif operation == 'multiply':
            pass
        elif operation == 'divide':
            pass
        else:
            newNum = 'Invalid Operation! Please try again.'
    else:
        pass
    
    return newNum

    