#
# day1 advent of code
# by Centopus
# in python
# 2023.12.02
#

input = open('inputFile','r')
counter = 0

while True:
    counter +=1

    line = input.readline()

    if not line:
        break
    print(line)

input.close()
