#
# day7 advent of code
# by Centopus
# in python
# 2023.12.07
#

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data

#data
data = readInput('inputMini')
#data = readInput('inputFile')

def numbers(line):
    numbers = line.split(' ')
    numbers = [i for i in numbers if i != '']
    return numbers

def parsing(line):
    out = line.split(':')
    data_tag = (out[0])
    data = numbers(out[1])
    return data


#main
print(output)

