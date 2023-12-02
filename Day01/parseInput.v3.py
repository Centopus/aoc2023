#
# day1 advent of code
# by Centopus
# in python
# 2023.12.02
#
import re

#input = open('inputFile','r')
input = open('miniPut','r')
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
    #we will translate words into digits and reuse code
    line = line.replace('one','1')
    line = line.replace('two','2')
    line = line.replace('three','3')
    line = line.replace('four','4')
    line = line.replace('five','5')
    line = line.replace('six','6')
    line = line.replace('seven','7')
    line = line.replace('eight','8')
    line = line.replace('nine','9')
    #this is lazyyyy ;D

    #print(line)
    print(line)
    out = p1.findall(line)
    #print(line)
    #we need first digit
    #print(out[0])
    #we need last digit
    #print(out[len(out)-1])
    #we need concatenate those
    tuple = out[0] + out[len(out)-1]
    print(tuple)
    
    output += int(tuple)
    #print(output)
    

input.close()
print(output)

