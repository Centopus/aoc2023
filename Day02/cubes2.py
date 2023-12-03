#
# day2 advent of code
# by Centopus
# in python
# 2023.12.02
#
import re


#data
#input = open('inputMini','r')
input = open('inputFile','r')

output = 0

while True:
    line = input.readline()

    if not line:
        break
    #we do not want the new line
    line = line.rstrip()
    print(line)
    # Game goes into 1 side, rest goes to the other side
    out = line.split(':')
    #we get the game number
    GameNr = int(out[0].strip('Game '))
    print(GameNr)
    #now we split the sets with semicolon
    out = out[1].split(';')
    #now we iterate over the split sets

    #limits_to_find_out
    red_l = 0
    green_l = 0
    blue_l = 0
    for reach in out:
        #print(reach)
        for item in reach.split(','):
            #print(item)
            liczba = item.split(' ')
            if item.endswith('red'):
                if int(liczba[1]) > red_l:
                    red_l = int(liczba[1])
            elif item.endswith('blue'):
                if int(liczba[1]) > blue_l:
                    blue_l = int(liczba[1])
            else:
                if int(liczba[1]) > green_l:
                    green_l = int(liczba[1])
    print('Game '+str(GameNr)+'R: '+str(red_l)+'B: '+str(blue_l)+'G: '+str(green_l))
    power = red_l*blue_l*green_l
    print(power)
    output += power
print(output)
