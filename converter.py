from math import *

def convert(line):
    if '<' in line:
        newLineList = line.split('<')
        newLine = "".join(newLineList)
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
    return newLine