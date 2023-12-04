#
# day4 advent of code
# by Centopus
# in python
# 2023.12.02
#

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data

#data = readInput('inputMini')
data = readInput('inputFile')

def parseData(line):
    out = line.split(':')
    CardNr = int(out[0].strip('Card '))
    out = out[1].split('|')
    winners = out[0].strip().split(' ')
    draws = out[1].strip().split(' ')
    winners = [i for i in winners if i is not None]
    winners = [i for i in winners if i != '']
    draws = [i for i in draws if i is not None]
    draws = [i for i in draws if i != '']
    return winners,draws

count = [1]*len(data)
j= [1]*len(data)
print(j)
print(count)

for i in range(len(data)):
    j[i] = i
    count[i] = 1

for i in j:
    wins = 0
    winners,draws = parseData(data[i])
    for draw in draws:
        if draw in winners:
            wins += 1
    secondIterator = i+1
    print('Wins: '+str(wins))
    while wins > 0:
        print(count[secondIterator])
        count[secondIterator] = count[secondIterator] + count[i]
        wins -= 1
        secondIterator += 1

output=0
for i in count:
    output += i
print(output)
