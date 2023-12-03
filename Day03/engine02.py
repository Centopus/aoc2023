#
# day3 advent of code
# by Centopus
# in python
# 2023.12.03
#
import re

#data
inputF = open('inputMini','r')
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
    numberComplex = di.search(line2)
    if numberComplex:
        start = numberComplex.start()
        end = numberComplex.end()
        check1 = line1[start-1:end+1]
        check2 = line2[start-1:start]+''.rjust(end-start,'.')+line2[end:end+1]
        check3 = line3[start-1:end+1]
        
        #print(check1)
        #print(check2)
        #print(check3)
        if ds.search(check1):
            #found something in first line
            #print(line2[start:end])
            output +=int(line2[start:end])
        elif ds.search(check2):
            #found something in second line
            #print(line2[start:end])
            output +=int(line2[start:end])
        elif ds.search(check3):
            #found something in third line
            #print(line2[start:end])
            output +=int(line2[start:end])
        #else:
            #print('do nothing')
            #found nothing - lonely number!
        
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

