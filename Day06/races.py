#
# day6 advent of code
# by Centopus
# in python
# 2023.12.06
#

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data

#data
data = readInput('inputMini')
data = readInput('inputFile')

def numbers(line):
    numbers = line.split(' ')
    numbers = [i for i in numbers if i != '']
    return numbers

def parsing(line):
    out = line.split(':')
    data_tag = (out[0])
    data = numbers(out[1])
    return data

def raceInc(Zeit,Strecke):
    time=int(Zeit)
    dist=int(Strecke)
    for chargetime in range(1,time,1):
        speed=chargetime;
        distance=speed*(time-chargetime);
        if distance > dist:
            #you win
            return chargetime

def raceDesc(Zeit,Strecke):
    time=int(Zeit)
    dist=int(Strecke)
    for chargetime in range(time,1,-1):
        speed=chargetime;
        distance=speed*(time-chargetime);
        if distance > dist:
            #you win
            return chargetime

#main
win=[]
Time=parsing(data[0])
Distance=parsing(data[1])
print(Time,Distance)
i=0
while i <= (len(data)+1):
    win.append([raceInc(Time[i],Distance[i]),raceDesc(Time[i],Distance[i])])
    i +=1
print(win)
output=1
for a in win:
    wins=0
    for b in range(a[0],a[1]+1,1):
        wins+=1
        #print(b)
    print(wins)
    output=output*wins
    #print(output)
print(output)

