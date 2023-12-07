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
def partition(array, low, high):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1



# function to perform quicksort
def quickSort(array, low, high):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

#comparison stuff goes here
#dictionary:
#A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

#the top most comparison function
def is_left_GT_right(cardL,cardR):
    answer = True
    return answer

def FiveOfKind(sequence):
    power = 7
    if sequence.count(sequence[0]) == 5:
        return power
    return 0

def FourOfKind(sequence):
    power = 6
    if sequence.count(sequence[0]) == 4:
        return power
    elif sequence.count(sequence[1]) == 4:
        return power
    return 0

def FullHouse(sequence):
    power = 5
    return 0

def ThreeOfKind(sequence):
    power = 4
    if sequence.count(sequence[0]) == 3:
        return power
    elif sequence.count(sequence[1]) == 3:
        return power
    elif sequence.count(sequence[2]) == 3:
        return power
    return 0

def TwoPair(sequence):
    power = 3
    return 0

def OnePair(sequence):
    power = 2
    if sequence.count(sequence[0]) == 2:
        return power
    elif sequence.count(sequence[1]) == 2:
        return power
    elif sequence.count(sequence[2]) == 2:
        return power
    elif sequence.count(sequence[3]) == 2:
        return power
    return 0

def HighCard(sequence):
    power = 1
    return 0

print(FiveOfKind('FFFFF'))
print(FiveOfKind('FFCFF'))
#thats from quicksort implementation... need to update it
#data = [1, 7, 4, 1, 10, 9, -2]
#print("Unsorted Array")
#print(data)
#size = len(data)
#quickSort(data, 0, size - 1)
#print('Sorted Array in Ascending Order:')
#print(data)

#to do ^^^

#main
cards=[]
for line in data:
    cards.append(numbers(line))
print(cards)

