#
# day3 advent of code
# by Centopus
# in python
# 2023.12.03
#
import re

#data
input = open('inputMini','r')
#input = open('inputFile','r')

#regex filters
di = re.compile(r'\d+')

output = 0

while True:
    line = input.readline()

    if not line:
        break
    #we do not want the new line
    line = line.rstrip()
    print(line)
    print(di.findall(line))
    numberComplex = di.search(line)
    if numberComplex:
        print(str(numberComplex.start()) +' to '+ str(numberComplex.end()))

