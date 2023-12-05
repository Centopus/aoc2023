#
# day5 advent of code
# by Centopus
# in python
# 2023.12.05
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

def seeds(line):
    out = line.split(':')
    seeds_tag = (out[0])
    seeds = numbers(out[1])
    return seeds

def mappa(data):

    return map1, map2


#main
print(seeds(data[0]))
