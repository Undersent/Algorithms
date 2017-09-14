complexityOfInsertion = []
complexityOfMerge = []
complexityOfQuick = []

swapsOfInsertion = []
swapsOfMerge = []
swapsOfQuick = []



def insertionSort(array):
    numberOfComp = 0
    numberOfSwap = 0
    for index in range(1,len(array)):
        curr = array[index]
        position = index
        numberOfComp += 1
        while position > 0 and array[position-1] > curr:
            #print("log for insertionSort:", array)
            array[position] = array[position-1]
            position = position - 1
            numberOfSwap += 1
            numberOfComp += 1
        array[position] = curr

    complexityOfInsertion.append(numberOfComp)
    swapsOfInsertion.append(numberOfSwap)
    return array



def quickSort(array):
    global numberOfCompQuick
    global numberOfSwapsQuick

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        #pivot = array[int(len(array)/2)]
        pivot = array[0]

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
            numberOfCompQuick += 1
        numberOfSwapsQuick +=1

       # print("log for quickSort: less", less," equal ", equal," greater ", greater, " aray ", array)

        return quickSort(less)+equal+quickSort(greater)  #the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  #when only have one element in array, just return the array.
        return array



def merge(a,b):

    global numberOfCompMerge
    global numberOfSwapsMerge
    c = []
    while len(a) != 0 and len(b) != 0:
        numberOfCompMerge += 1
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])

        else:
            c.append(b[0])
            b.remove(b[0])
            numberOfSwapsMerge += 1
    if len(a) == 0:
        c += b
        numberOfSwapsMerge += 1
    else:
        numberOfSwapsMerge += 1
        c += a
    return c

# Code for merge sort

def mergeSort(array):

    #global numberOfCompMerge
    if len(array) == 0 or len(array) == 1:
        return array
    else:
        middle = int(len(array)/2)
        a = mergeSort(array[:middle])
        b = mergeSort(array[middle:])
        #print("log for merge sort ", a,"  ", b)
        return merge(a,b)


def getArray(typeOfArray):
    if (typeOfArray == 1):
        return Generator.generateRandomNumbers(sizeOfData, min, max)
    elif (typeOfArray == 2):
        return Generator.generateSortedNumbers(sizeOfData, min, max)

def save(complexityOfInsertion,swapsOfInsertion, complexityOfQuick, swapsOfQuick, complexityOfMerge, swapsOfMerge):
    with open("complexityOfInsertion", 'w') as f:
        for s in complexityOfInsertion:
            f.write(str(s) + '\n')

    with open("swapsOfInsertion", 'w') as f:
        for s in swapsOfInsertion:
            f.write(str(s) + '\n')


    with open("complexityOfQuick", 'w') as f:
        for s in complexityOfQuick:
            f.write(str(s) + '\n')

    with open("swapsOfQuick", 'w') as f:
        for s in swapsOfQuick:
            f.write(str(s) + '\n')


    with open("complexityOfMerge", 'w') as f:
        for s in complexityOfMerge:
            f.write(str(s) + '\n')

    with open("swapsOfMerge", 'w') as f:
        for s in swapsOfMerge:
            f.write(str(s) + '\n')



size = 0  #rozmiar tablicy
min=1     #minimalna liczba w tablicy
max = 100000
typeOfArray = 2  # 1 - unsorted order, 2- reverse order

import resource
import sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

"""l = [2, 1, 5, 3, 9, 6, 7]
(insertionSort(l))
l = [2, 1, 5, 3, 9, 6, 7]
print(quickSort(l))
l = [2, 1, 5, 3, 9, 6, 7]
print(mergeSort(l))"""
#print(generator.generateRandomNumbers(10,10,100))
#print(generator.generateSortedNumbers(10,10,100))
"""size = int(input("1: Write size of your data "))
min = int(input("2: Write minimal number in your array "))
max = int(input("1: Write maximal number in your array "))
typeOfArray = int(input("1 - random order of array \n2 - sorted order of array "))"""


start = 100       # minimalny rozmiar tablicy
end = 10000
step = 100
array = None


if(min<max):


    for sizeOfData in range(start,end +1, step):
        print("counting for ", sizeOfData)

        #array = getArray(typeOfArray)
        #insertionSort(array)

        numberOfCompQuick = 0
        numberOfSwapsQuick = 0
        array = getArray(typeOfArray)
        quickSort(array)
        complexityOfQuick.append(numberOfCompQuick)
        swapsOfQuick.append(numberOfSwapsQuick)

        #numberOfCompMerge = 0
        #numberOfSwapsMerge = 0
        #array = getArray(typeOfArray)
        #mergeSort(array)
        #complexityOfMerge.append(numberOfCompMerge)
        #swapsOfMerge.append(numberOfSwapsMerge)

    print(complexityOfInsertion)
    print(complexityOfQuick)
    print(complexityOfMerge)

    save(complexityOfInsertion,swapsOfInsertion, complexityOfQuick,swapsOfQuick, complexityOfMerge, swapsOfMerge)

else:
    print ("min>max, End ")
