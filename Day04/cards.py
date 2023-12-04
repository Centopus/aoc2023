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
data = readInput('inputMini')
#data = readInput('inputFile')


output = 0

def parseData(line):
    out = line.split(':')
    CardNr = int(out[0].strip('Card '))

    out = out[1].split('|')
    #first set is winners, second set is draws
    winners = out[0].strip().split(' ')
    draws = out[1].strip().split(' ')
    print(winners)
    print(draws)
#it does live extra empty stuff i need to remove

    return winners,draws


#main

for line in data:
    print(line)
    winners,draws = parseData(line)

#while True:
#    line = input.readline()
#
#    if not line:
#        break
#    #we do not want the new line
#    line = line.rstrip()
#    print(line)
#    # Game goes into 1 side, rest goes to the other side
#    out = line.split(':')
#    #we get the game number
#    GameNr = int(out[0].strip('Game '))
#    print(GameNr)
#    #now we split the sets with semicolon
#    out = out[1].split(';')
#    #now we iterate over the split sets
#    GameOK = True
#    for reach in out:
#        #print(reach)
#        for item in reach.split(','):
#            #print(item)
#            liczba = item.split(' ')
#            if item.endswith('red'):
#                if int(liczba[1]) > red_l:
#                    print('ErrorR')
#                    GameOK = False
#            elif item.endswith('blue'):
#                if int(liczba[1]) > blue_l:
#                    print('ErrorB')
#                    GameOK = False
#            else:
#                if int(liczba[1]) > green_l:
#                    print('ErrorG')
#                    GameOK = False
#    if GameOK == True:
#        output += GameNr
#    print(output)
print(output)
