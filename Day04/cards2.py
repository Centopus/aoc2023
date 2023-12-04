#
# day4 advent of code
# by Centopus
# in python
# 2023.12.02
#

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data

#data
data = readInput('inputMini')
data = readInput('inputFile')

def parseData(line):
    out = line.split(':')
    CardNr = int(out[0].strip('Card '))

    out = out[1].split('|')
    #first set is winners, second set is draws
    winners = out[0].strip().split(' ')
    draws = out[1].strip().split(' ')
    #i need to read more about this filter function, now i just took it as in an example
    #winners = list(filter(lambda item: item is not None, winners))
    winners = [i for i in winners if i is not None]
    winners = [i for i in winners if i != '']
    #draws = list(filter(lambda item: item is not None, draws))
    draws = [i for i in draws if i is not None]
    draws = [i for i in draws if i != '']
    #print(winners)
    #print(draws)
    return winners,draws

#this adds two collumns to my list, so i can store how many 'cards' i get and index of the row
def formatData(data):
    count = []*len(data)
    j = []*len(data)
    for i in range(len(data)):
        j[i] = i
        count[i] = 1
#    cardData = (list(zip(ident, count, data)))
    return j,count

#main

#j,count = formatData(data)

count = [1]*len(data)
j= [1]*len(data)
print(j)
print(count)

for i in range(len(data)):
    j[i] = i
    count[i] = 1

print(j)
print(count)

#print('this is the iterator collumn   ' +str(cardData[0][0])) 
#print('this is the counter collumn    ' +str(cardData[0][1])) 
#print('this is the data collumn       ' +str(cardData[0][2])) 
#print('this is the data collumn too   ' +str(cardData[1][2])) 

#cardData[0][1] = cardData[0][1] + 7


#for i,counter,line in j,count,data:
for i in j:
    #print(i)
    #print(counter)
    #print(line)
    wins = 0
    winners,draws = parseData(data[i])
    for draw in draws:
        if draw in winners:
            wins += 1
    secondIterator = i+1
    print('Wins: '+str(wins))
    while wins > 0:
        print(count[secondIterator])
        count[secondIterator] = count[secondIterator] + count[i]
        wins -= 1
        secondIterator += 1

output=0
for i in count:
    output += i
print(output)

#for line in data:
#    print(line)
#    victory = 0
#    first = True
#    winners,draws = parseData(line)
#    for draw in draws:
#        if draw in winners:
#            if first is True:
#                victory = 1
#                first = False
#            else:
#                victory = victory*2
#    print(victory)
#    output = output + victory
#print(output)
