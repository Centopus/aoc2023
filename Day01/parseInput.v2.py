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

#patterns need to be compiled before can be used
#single digit
p1= re.compile('[0-9]{1}')

while True:
    counter += 1

    line = input.readline()

    if not line:
        break
    
    out = p1.match(line)
    print(line)
    print(out)

input.close()
