#
# day2 advent of code
# by Centopus
# in python
# 2023.12.02
#

#data
#input = open('inputMini','r')
#input = open('inputFile','r')

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data


data = readInput('inputMini')
for lineID, line in enumerate(data):
    print(lineID, line)

output = 0

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
