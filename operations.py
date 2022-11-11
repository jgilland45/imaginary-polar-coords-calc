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
        imaginary1 = num1List[1][0:len(num1List[1])-1]
        real2 = num2List[0]
        imaginary2 = num2List[1][0:len(num2List[1])-1]
        
        if operation == 'add':
            real = float(real1) + float(real2)
            imaginary = float(imaginary1) + float(imaginary2)
            if imaginary>=0:
                newNum = str(real) + '+' + str(imaginary) + 'j'
            else:
                newNum = str(real) + '-' + str(abs(imaginary)) + 'j'
        elif operation == 'subtract':
            real = float(real1) - float(real2)
            imaginary = float(imaginary1) - float(imaginary2)
            if imaginary>=0:
                newNum = str(real) + '+' + str(imaginary) + 'j'
            else:
                newNum = str(real) + '-' + str(abs(imaginary)) + 'j'
        elif operation == 'multiply':
            real = (float(real1) * float(real2)) - (float(imaginary1) * float(imaginary2))
            imaginary = (float(real1) * float(imaginary2)) + (float(real2) * float(imaginary1))
            if imaginary>=0:
                newNum = str(real) + '+' + str(imaginary) + 'j'
            else:
                newNum = str(real) + '-' + str(abs(imaginary)) + 'j'
        elif operation == 'divide':
            numeratorReal = (float(real1) * float(real2)) - (float(imaginary1) * -float(imaginary2))
            numeratorImaginary = (float(real1) * -float(imaginary2)) + (float(real2) * float(imaginary1))
            denominator = (float(real2)**2) + (float(imaginary1)**2)
            real = numeratorReal/denominator
            imaginary = numeratorImaginary/denominator
            if imaginary>=0:
                newNum = str(real) + '+' + str(imaginary) + 'j'
            else:
                newNum = str(real) + '-' + str(abs(imaginary)) + 'j'
        else:
            newNum = 'Invalid Operation! Please try again.'
    else:
        pass
    
    return newNum

    