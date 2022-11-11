from math import *

def convert(line, convertType):
    if convertType == 'polar':
        if '<' in line:
            newLine = line
        elif '+' in line or '-' in line:
            if '+' in line:
                newLineList = line.split('+')
            elif '-' in line:
                newLineList = line.split('-')
            amplitude = sqrt((float(newLineList[0])**2) + (float(newLineList[1][0:len(newLineList[1])-1])**2))
            if float(newLineList[0]) != 0.0:
                angle = atan(float(newLineList[1][0:len(newLineList[1])-1])/float(newLineList[0]))
            else:
                if '+' in line:
                    angle = pi/2
                elif '-' in line:
                    angle = -pi/2
            newLine = str(amplitude) + '<' + str(degrees(angle))
        else:
            newLine = "Invalid Input! Try again."
    elif convertType == 'imaginary':
        if '<' in line:
            newLineList = line.split('<')
            real = float(newLineList[0]) * cos(radians(float(newLineList[1])))
            imaginary = float(newLineList[0]) * sin(radians(float(newLineList[1])))
            if imaginary>=0:
                newLine = str(real) + '+' + str(imaginary) + 'j'
            else:
                newLine = str(real) + '-' + str(abs(imaginary)) + 'j'
        elif '+' in line or '-' in line:
            newLine = line
        else:
            newLine = "Invalid Input! Try again."
    else:
        newLine = "Invalid Input! Try again."
    return newLine