#
# day1 advent of code
# by Centopus
# in python
# 2023.12.02
#
import re

input = open('inputFile','r')
#input = open('miniPut','r')
counter = 0
output = 0

#patterns need to be compiled before can be used
#single digit
p1= re.compile('[0-9]{1}')

while True:
    counter += 1

    line = input.readline()

    if not line:
        break
    
    out = p1.findall(line)
    #print(line)
    #we need first digit
    #print(out[0])
    #we need last digit
    #print(out[len(out)-1])
    #we need concatenate those
    tuple = out[0] + out[len(out)-1]
    #print(tuple)
    
    output += int(tuple)
    print(output)
    

input.close()
