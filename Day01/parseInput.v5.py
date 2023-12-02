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
#p1= re.compile('[0-9]{1}')
p1= re.compile('one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9')
p2= re.compile(r'one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9')

while True:
    counter += 1

    line = input.readline()

    if not line:
        break

    #print(line)
    print('Line: '+line)
    out = p1.findall(line)
    out2 = p2.search(line)
    #print('First: ')
    #print(out[0])
    print('Last: ')
    print(out[len(out)-1])
    print('out2: ')
    print(out2)
    #we need concatenate those
    twin = out[0] + out[len(out)-1]
    print('Tuple: ')
    print(twin)
    
    twin = twin.replace('one','1')
    twin = twin.replace('two','2')
    twin = twin.replace('three','3')
    twin = twin.replace('four','4')
    twin = twin.replace('five','5')
    twin = twin.replace('six','6')
    twin = twin.replace('seven','7')
    twin = twin.replace('eight','8')
    twin = twin.replace('nine','9')
    print(twin)
    output += int(twin)
    #print(output)
    

input.close()
print(output)

