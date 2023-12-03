#
# day3 advent of code
# by Centopus
# in python
# 2023.12.03
#
import re

#data
#inputF = open('inputMini','r')
#inputF = open('inputMini2','r')
inputF = open('inputMini3','r')
#inputF = open('inputFile','r')

#regex filters
di = re.compile(r'\d+')
ds = re.compile(r'[^.]')
da = re.compile(r'[*]')

#funtions, well i need to recurse stuff... its easier with funtions
#funny how python forces you to funtionize once you using multiple layers of loops
#because managing multiple levels of indentation is pain

#this one should do the parsing, this is going to be a recursive thing
def searchFurNum(line1,line2,line3,output):
    restOfLine = ''
    numberComplex = da.search(line2)
    if numberComplex:
        start = numberComplex.start()
        end = numberComplex.end()
        check1 = line1[start-3:end+3]
        check2a = line2[start-3:start]
        check2b = line2[end:end+3]
        check3 = line3[start-3:end+3]
        power = 1
        found = 0

        if di.search(check1):
            first = di.search(check1)
            fend = first.end()
            second = di.search(check1[fend:end+3])
            # start needs to be in fields 2,3,4 or end in 3,4,5
            if fend in (3,4,5) or first.start() in (2,3,4):
                print('c1int: '+check1[first.start():first.end()])
                power = power*int(check1[first.start():first.end()])
                found +=1
            # need to check other part of the string
            elif second:
                if second.end() in (3-fend,4-fend,5-fend) or second.start() in (2-fend,3-fend,4-fend):
                    print('c1bint: '+check1[fend+second.start():fend+second.end()])
                    power = power*int(check1[fend+second.start():fend+second.end()])
                    found +=1
                #second hit check same check
        if di.search(check2a):
            first = di.search(check2a)
            fend = first.end()
            # needs to be in fields 2
            if fend == 3:
                print('c2int: '+check2a[first.start():first.end()])
                power = power*int(check2a[first.start():first.end()])
                found +=1
                #output +=int(line2[start:end])
        if di.search(check2b):
            first = di.search(check2b)
            # needs to be in fields 0
            if first.start() == 0:
                print('c2bint: '+check2b[first.start():first.end()])
                power = power*int(check2b[first.start():first.end()])
                found +=1
        if di.search(check3):
            first = di.search(check3)
            fend = first.end()
            second = di.search(check3[fend:end+3])
            # start needs to be in fields 2,3,4 or end in 3,4,5
            if fend in (3,4,5) or first.start() in (2,3,4):
                print('c3int: '+check3[first.start():first.end()])
                power = power*int(check3[first.start():first.end()])
                found +=1
            # need to check other part of the string
            elif second:
                if second.end() in (3-fend,4-fend,5-fend) or second.start() in (2-fend,3-fend,4-fend):
                    #print('c3b: '+line3[first.end():end+3])
                    power = power*int(check3[fend+second.start():fend+second.end()])
                    found +=1
                    print('c3bint: '+check3[fend+second.start():fend+second.end()])
        if found == 2:
            print(power)
            output += power
        elif found == 3:
            print('WAAAAAAt')
        
        LLen = len(line1)

        #here happens the magix
        output = searchFurNum(line1[end:LLen],line2[end:LLen],line3[end:LLen],output)

    return output

#this one should prepare the lines for parsing
def threeLines(line1,line2,inputF,loopVar):
    aLine = line1;
    bLine = line2;
    cLine = inputF.readline()
    if not cLine:
        #if its the last one, we will full it with dots just like the first one
        cLine=''.rjust(lineLen+2,'.')
        loopVar = False
    cLine = cLine.rstrip().rjust(lineLen+1,'.').ljust(lineLen+1,'.')
    return aLine,bLine,cLine,loopVar

#here goes "main" 
output = 0
#we need to go 3 lines in a loop to check for adjacent symbols
#we need the first line to start... and to initialize stuff
#and run the first line parsing
bLine = inputF.readline()
cLine = inputF.readline()
lineLen = len(bLine)
#i'm padding the outsides with '.' so i need not make special cases for sides
bLine = bLine.rstrip().rjust(lineLen+1,'.').ljust(lineLen+1,'.')
cLine = cLine.rstrip().rjust(lineLen+1,'.').ljust(lineLen+1,'.')
aLine = ''.rjust(lineLen+2,'.')
#print(aLine +' '+ bLine +' '+ cLine)
output = searchFurNum(aLine,bLine,cLine,output)
#main loop
loopVar = True
while loopVar:
    aLine,bLine,cLine,loopVar = threeLines(bLine,cLine,inputF,loopVar)
    #print(aLine +' '+ bLine +' '+ cLine)
    output = searchFurNum(aLine,bLine,cLine,output)
print(output)

