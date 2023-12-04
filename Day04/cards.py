#
# day2 advent of code
# by Centopus
# in python
# 2023.12.02
#

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data

#data
#data = readInput('inputMini')
data = readInput('inputFile')


output = 0

def parseData(line):
    out = line.split(':')
    CardNr = int(out[0].strip('Card '))

    out = out[1].split('|')
    #first set is winners, second set is draws
    winners = out[0].strip().split(' ')
    draws = out[1].strip().split(' ')
    #i need to read more about this filter function, now i just took it as in an example
    #winners = list(filter(lambda item: item is not None, winners))
    winners = [i for i in winners if i is not None]
    winners = [i for i in winners if i is not '']
    #draws = list(filter(lambda item: item is not None, draws))
    draws = [i for i in draws if i is not None]
    draws = [i for i in draws if i is not '']
    print(winners)
    print(draws)
    return winners,draws


#main

output=0
for line in data:
    print(line)
    victory = 0
    first = True
    winners,draws = parseData(line)
    for draw in draws:
        if draw in winners:
            if first is True:
                victory = 1
                first = False
            else:
                victory = victory*2
    print(victory)
    output = output + victory
print(output)
