#
# day5 advent of code
# by Centopus
# in python
# 2023.12.05
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

def seeds(line):
    out = line.split(':')
    seeds_tag = (out[0])
    seeds = numbers(out[1])
    return seeds

def mappa(data,i):
    map_name=data[i]
    map_objects=[]
    #print('Map Name: '+map_name)
    while True:
        i += 1
        if i+1>len(data):
            break
        elif data[i] == '':
            break
        num=numbers(data[i])
        map_objects.append(num)
    #print(map_objects)
    return map_name, map_objects

def seed2location(seedid,book):
    seedid=int(seedid)
    for mapitem in book:
        #print(mapitem[1])
        for page in mapitem[1]:
            start = int(page[1])
            end = int(page[1])+int(page[2])
            delta = int(page[0])
            #print('start :'+str(start)+' end: '+str(end))
            if seedid >= start and seedid <= end:
                increment = seedid - start
                seedid = delta + increment
                break
                #print(seedid)
            #else:
            #print(seedid)
            #print(page)

    return seedid

def seedGenerator(seeds,output,book):
    for i in range(0,len(seeds),2):
        start = int(seeds[i])
        count = int(seeds[i+1])
        for j in range(start,count+start,1):
            #print(j)
            temp = seed2location(j,book)
            #print('t '+str(temp))
            if output > temp:
                output = temp
                #print('out:'+str(output))
    return output

#main

#we get our map starts - detection where empty lines are.
starts = []
for i,line in enumerate(data):
    if line == '':
        starts.append(i)
book=[]
#book[map choice][0-name,1-map][0..X-lines of map][elements of line]
#we read our data and fill in the translation book
for i in starts:
    book.append(mappa(data,i+1))

#print(book)
#print(book[0][0]) #name
#print(book[0][1]) #whole map
#print(book[0][1][0]) #first line of map
#print(book[0][1][0][0]) #single digt of map?
#book[map choice][0-name,1-map][0..X-lines of map][o-destination 1- source 2- length]

#print(seeds(data[0]))
#print(seedGenerator(seeds(data[0])))

#seed2location(14,book)
output = 9999999999999999

output = seedGenerator(seeds(data[0]),output,book)
print(output)

