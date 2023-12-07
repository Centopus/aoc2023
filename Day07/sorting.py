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
data = readInput('inputMini')
#data = readInput('inputFile')

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
    power = 70
    if sequence.count(sequence[0]) == 5:
        return power
    return 0

def FourOfKind(sequence):
    power = 60
    if sequence.count(sequence[0]) == 4:
        return power
    elif sequence.count(sequence[1]) == 4:
        return power
    return 0

def FullHouse(sequence):
    #also does 3 of a Kind
    power = 50
    if sequence.count(sequence[0]) == 3:
        sequence = sequence.replace(sequence[0],'')
        #print(sequence)
        if sequence.count(sequence[0]) == 2:
            return power
        else:
            return 40
    elif sequence.count(sequence[1]) == 3:
        sequence = sequence.replace(sequence[1],'')
        if sequence.count(sequence[0]) == 2:
            return power
        else:
            return 40
    elif sequence.count(sequence[2]) == 3:
        sequence = sequence.replace(sequence[2],'')
        if sequence.count(sequence[0]) == 2:
            return power
        else:
            return 40
    #at this point we have 3 and removed them
    return 0

def TwoPair(sequence):
    power = 30
    if sequence.count(sequence[0]) == 2:
        sequence = sequence.replace(sequence[0],'')
        if sequence.count(sequence[0]) == 2:
            return power
        elif sequence.count(sequence[1]) == 2:
            return power
        else:
            #single pair
            return 20
    elif sequence.count(sequence[1]) == 2:
        sequence = sequence.replace(sequence[1],'')
        if sequence.count(sequence[0]) == 2:
            return power
        elif sequence.count(sequence[1]) == 2:
            return power
        return 20
    elif sequence.count(sequence[3]) == 2:
        return 20
    elif sequence.count(sequence[4]) == 2:
        return 20

    return 0

#we need to rank this too...
#and this will be nice to rank same power things
#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
#14, 13, 12, 11, 10
def HighCard(sequence):
    if 'A' in sequence:
        return 14
    elif 'K' in sequence:
        return 13
    elif 'Q' in sequence:
        return 12
    elif 'J' in sequence:
        return 11
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
    else:
        return 2
    return 2

def rankCard(sequence):
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
#i=0
#while i < len(cards):
#    print(is_left_GT_right(cards[i],powers[i],cards[1],powers[1]))
#    i +=1
print('----------------------------')
quickSort(cards,powers,bets,0,size -1)
i=0
while i < size:
    print(cards[i]+' : '+bets[i] + ' :: ' + str(powers[i]))
    i += 1
i=0
suma=0
while i < size:
#    print(bets[i])
#    print(i+1)
    suma = suma + int(bets[i])*(i+1)
#    print(suma)
    i += 1
print(suma)

