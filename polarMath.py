from converter import *
from operations import *

convertType = input("What type would you like your answer in? (polar or imaginary) ").strip()
operationType = input("What operation would you like to do? (add, subtract, multiply, divide) ").strip()
numberOne = input("Enter first polar number: ").strip()
numberTwo = input("Enter second polar number: ").strip()

convertedOne = convert(numberOne, convertType)
convertedTwo = convert(numberTwo, convertType)

finalNum = operate(convertedOne, convertedTwo, convertType, operationType)
print(finalNum)

