#
# day7 advent of code
# by Centopus
# in python
# 2023.12.07
#

def readInput(filename):
    with open(filename) as var1:
        data = [line.rstrip() for line in var1.readlines()]
    return data

#data
#data = readInput('inputMini')
#data = readInput('inputMicro')
#data = readInput('inputReddit_1343')
#data = readInput('inputSwe_251136060')
#data = readInput('inputWrald')
data = readInput('inputFile')

def numbers(line):
    numbers = line.split(' ')
    numbers = [i for i in numbers if i != '']
    return numbers


# Function to find the partition position
def partition(array,powers,bets, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]
    powerPivot = powers[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
#        if array[j] <= pivot:
        if not is_left_GT_right(array[j],powers[j],pivot,powerPivot):

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            ( array[i],  array[j]) = ( array[j],  array[i])
            (powers[i], powers[j]) = (powers[j], powers[i])
            (  bets[i],   bets[j]) = (  bets[j],   bets[i])

    # Swap the pivot element with the greater element specified by i
    ( array[i + 1],  array[high]) = ( array[high],  array[i + 1])
    (powers[i + 1], powers[high]) = (powers[high], powers[i + 1])
    (  bets[i + 1],   bets[high]) = (  bets[high],   bets[i + 1])

    # Return the position from where partition is done
    return i + 1



# function to perform quicksort
def quickSort(array,powers,bets, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array,powers,bets, low, high)

        # Recursive call on the left of pivot
        quickSort(array,powers,bets, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array,powers,bets, pi + 1, high)

#comparison stuff goes here
#dictionary:
#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

#the top most comparison function
def is_left_GT_right(cardL,powerL,cardR,powerR):
    if powerL > powerR:
        return True
    elif powerL < powerR:
        return False
    else:
        i=0
        while i < 5:
            #print('comparing '+ str(cardL[i])+ ' '+ str(cardR[i]))
            if HighCard(cardL[i]) > HighCard(cardR[i]):
                return True
            elif HighCard(cardL[i]) < HighCard(cardR[i]):
                return False
            i += 1
    return True

def FiveOfKind(sequence):
    if sequence.count(sequence[0]) == 5:
        if sequence[0] == 'J':
            return 69
        return 70
    return 0

def FourOfKind(sequence):
    if sequence.count(sequence[0]) == 4:
        if sequence[0] == 'J':
            return 69
        sequence = sequence.replace(sequence[0],'')
        if sequence[0] == 'J':
            return 69
        return 60
    elif sequence.count(sequence[1]) == 4:
        if sequence[1] == 'J':
            return 69
        if sequence[0] == 'J':
            return 69
        return 60
    return 0

def FullHouse(sequence):
    if sequence.count(sequence[0]) == 3:
        temp = sequence[0]
        sequence = sequence.replace(sequence[0],'')
        if sequence.count(sequence[0]) == 2:
            if temp == 'J' or sequence[0] == 'J':
                return 69
            return 50
        else:
            if temp == 'J':
                return 49
            elif sequence[0] == 'J' or sequence[1] == 'J':
                return 49
            return 40
    elif sequence.count(sequence[1]) == 3:
        temp = sequence[1]
        sequence = sequence.replace(sequence[1],'')
        if sequence.count(sequence[0]) == 2:
            if temp == 'J' or sequence[0] == 'J':
                return 69
            return 50
        else:
            if temp == 'J':
                return 49
            elif sequence[0] == 'J' or sequence[1] == 'J':
                return 49
            return 40
    elif sequence.count(sequence[2]) == 3:
        temp = sequence[2]
        sequence = sequence.replace(sequence[2],'')
        if sequence.count(sequence[0]) == 2:
            if temp == 'J' or sequence[0] == 'J':
                return 69
            return 50
        else:
            if temp == 'J':
                return 49
            elif sequence[0] == 'J' or sequence[1] == 'J':
                return 49
            return 40
    return 0

def TwoPair(sequence):
    if sequence.count(sequence[0]) == 2:
        temp = sequence[0]
        sequence = sequence.replace(sequence[0],'')
        if sequence.count(sequence[0]) == 2:
            if temp == 'J':
                #4ofkind
                return 59
            elif sequence[0] == 'J':
                #4ofkind
                return 59
            elif sequence.replace(sequence[0],'')[0] == 'J':
                #full
                return 49
            #2pair
            return 30
        elif sequence.count(sequence[1]) == 2:
            if sequence[1] == 'J':
                #4ofkind
                return 59
            elif sequence[0] == 'J':
                #full
                return 49
            #2pair
            return 30
        else:
            #joker check here
            if temp == 'J':
                #3ofK
                return 39
            elif sequence.count('J') > 0:
                #3ofk
                return 39
            return 20
    elif sequence.count(sequence[1]) == 2:
        temp = sequence[1]
        sequence = sequence.replace(sequence[1],'')
        if sequence.count(sequence[0]) == 2:
            if temp == 'J' or sequence[0] == 'J':
                #4ofkind
                return 59
            elif sequence.replace(sequence[0],'')[0] == 'J':
                #full
                return 49
            #2pair
            return 30
        elif sequence.count(sequence[1]) == 2:
            if temp == 'J' or sequence[1] == 'J':
                #4ofk
                return 59
            elif sequence.replace(sequence[1],'')[0] == 'J':
                #full
                return 49
            #2pair
            return 30
        else:
            #joker check here
            if temp == 'J':
                #3ofK
                return 39
            elif sequence.count('J') > 0:
                #3ofk
                return 39
            return 20
    elif sequence.count(sequence[2]) == 2:
        if sequence[2] == 'J':
            #3ofk
            return 39
        elif sequence.replace(sequence[2],'').count('J') > 0:
            #3ofk
            return 39
        return 20
    elif sequence.count(sequence[3]) == 2:
        if sequence[3] == 'J':
            #3ofk
            return 39
        elif sequence.replace(sequence[3],'').count('J') > 0:
            #3ofk
            return 39
        return 20
    #joker detection here
    if sequence.count('J') > 0:
        #pair
        return 19
    return 10

#we need to rank this too...
#and this will be nice to rank same power things
# A,  K,  Q,  J,  T, 9, 8, 7, 6, 5, 4, 3, 2
#14, 13, 12, 11, 10
def HighCard(sequence):
    if 'A' in sequence:
        return 14
    elif 'K' in sequence:
        return 13
    elif 'Q' in sequence:
        return 12
    #elif 'J' in sequence:
    #    return 11
    elif 'T' in sequence:
        return 10
    elif '9' in sequence:
        return 9
    elif '8' in sequence:
        return 8
    elif '7' in sequence:
        return 7
    elif '6' in sequence:
        return 6
    elif '5' in sequence:
        return 5
    elif '4' in sequence:
        return 4
    elif '3' in sequence:
        return 3
    elif '2' in sequence:
        return 2
    #Joker left...
    return 1

def rankCard(sequence):
    temp = 0
    temp = FiveOfKind(sequence)
    if temp > 0:
        return temp
    temp = FourOfKind(sequence)
    if temp > 0:
        return temp
    temp = FullHouse(sequence)
    if temp > 0:
        return temp
    temp = TwoPair(sequence)
    if temp > 0:
        return temp
    temp = HighCard(sequence)
    return temp


#main
cards=[]
bets=[]
powers=[]
for line in data:
    cards.append(numbers(line)[0])
    bets.append(numbers(line)[1])
for card in cards:
    powers.append(rankCard(card))
#print(cards) #,powers,bets)
#print(powers)
#print(bets)
i=0
size = len(cards)
while i < size:
    print( cards[i]+' : ' + bets[i] + ' :: ' + str(powers[i]) )
    i +=1
print('----------------------------')
quickSort(cards,powers,bets,0,size -1)
i=0
while i < size:
    print(cards[i]+' : '+bets[i] + ' :: ' + str(powers[i]))
    i += 1
i=0
suma=0
while i < size:
    #print(bets[i])
    suma = suma + int(bets[i])*(i+1)
    i += 1
print(suma)

#print(rankCard('JJJAJ'))
