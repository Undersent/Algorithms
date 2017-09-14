from Lista2 import Generator


def insertionSortNP(array):

    start = time.clock()


    numberOfShifting = 0
    for index in range(1,array.size):
        curr = array[0,index]
        position = index


        while position > 0 and array[0,position-1] > curr:
            #print("log for insertionSort:", array)
            array[0,position] = array[0,position-1]
            position = position - 1
            numberOfShifting+=1


        array[0,position] = curr
   # complexityOfInsertion.append(numberOfShifting)
    print(time.clock() - start)

    return array


def insertionSort2(array):
    start = time.clock()
    numberOfShifting = 0
    for index in range(1,len(array)):
        curr = array[index]
        position = index

        while position > 0 and array[position-1] > curr:
            #print("log for insertionSort:", array)
            array[position] = array[position-1]
            position = position - 1
            numberOfShifting+=1


        array[position] = curr
    #complexityOfInsertion.append(numberOfShifting)
    print(time.clock() - start)
    return array
"""

array = np.random.random_integers(low=1, high=10000, size=(1, 100000))
array2 = Generator.generateRandomNumbers(100000, 1 , 100000)
#print(array)
#print (array[0,1])
#insertionSortNP(array)
insertionSortNP(array)
insertionSort(array2)"""
"""
complexityOfInsertion = []
complexityOfMerge = []
complexityOfQuick = []

swapsOfInsertion = []
swapsOfMerge = []
swapsOfQuick = []
"""
def quickSort(array):
    #global numberOfCompQuick
    #global numberOfSwapsQuick

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[int(len(array)/2)]

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
           # numberOfCompQuick += 1
        #numberOfSwapsQuick +=1
        # Don't forget to return something!
       # print("log for quickSort: less", less," equal ", equal," greater ", greater, " aray ", array)
        #numberOfSwapsQuick += len(less) + len(greater)
        return quickSort(less)+equal+quickSort(greater)  #the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  #when only have one element in array, just return the array.
        return array

numberOfSwapsQuick = 0
numberOfCompQuick = 0
numberOfCompMerge = 0
numberOfSwapsMerge = 0
"""
def merge(a,b):


    c = []
    while len(a) != 0 and len(b) != 0:

        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])

        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        c += b

    else:

        c += a
    return c
"""
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

"""
l= [ 15, 5, 1, 0, 20, 25, 30, 35, 40]  #comp 25, swaps 7
p = [1,2,3,4,5,6,7,8]
#quickSort(l)
print(quickSort(l))
print(numberOfCompMerge)
print(numberOfSwapsMerge)
"""

complexityOfHybrid = []
swapsOfHybrid = []

def insertionSort(array):
    #global numberOfCompHybrid
    #global numberOfSwapsHybrid
    for index in range(1,len(array)):
        curr = array[index]
        position = index
        #numberOfCompHybrid += 1
        while position > 0 and array[position-1] > curr:
            #print("log for insertionSort:", array)
            array[position] = array[position-1]
            position = position - 1
            #numberOfSwapsHybrid += 1
            #numberOfCompHybrid += 1
        array[position] = curr

    #complexityOfHybrid.append(numberOfCompHybrid)
    #swapsOfHybrid.append(numberOfSwapsHybrid)
    return array



def quickSortHybrid(array):
    #global numberOfCompHybrid
    #global numberOfSwapsHybrid

    less = []
    equal = []
    greater = []

    if len(array) > 8:
        pivot = array[int(len(array)/2)]

        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quickSortHybrid(less)+equal+quickSortHybrid(greater)  #the + operator to join lists
    elif len(array) <= 7:
        return insertionSort(array)

    else:
        return array


def merge(a,b):

    c = []
    while len(a) != 0 and len(b) != 0:

        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])

        else:
            c.append(b[0])
            b.remove(b[0])

    if len(a) == 0:
        c += b

    else:

        c += a
    return c

# Code for merge sort

def mergeSortHybrid(array):

    #global numberOfCompMerge

    if len(array) == 0 or len(array) == 1:
        return array
    if len(array) < 8:
        return insertionSort(array)
    else:
        middle = int(len(array)/2)
        a = mergeSortHybrid(array[:middle])
        b = mergeSortHybrid(array[middle:])
        #print("log for merge sort ", a,"  ", b)
        return merge(a,b)





numberOfCompHybrid = 0
numberOfSwapsHybrid = 0
array = Generator.generateRandomNumbers(10000, 1, 100000)
import time
start = time.clock()
quickSortHybrid(array)
#print(time.clock() - start)
#print(numberOfCompHybrid)
#print(numberOfSwapsHybrid)



numberOfCompQuick=0
numberOfSwapsQuick=0

array = Generator.generateRandomNumbers(10000, 1, 100000)
start = time.clock()
quickSort(array)
#print(time.clock() - start)
print(mergeSortHybrid(array))
"""
"""
with open("complexityOfHybridQuickInsertion", 'w') as f:
    for s in complexityOfHybrid:
        f.write(str(s) + '\n')
with open("SwapsOfHybridQuickInsertion", 'w') as f:
    for s in swapsOfHybrid:
        f.write(str(s) + '\n')


quickTimer = 0
quickInsTimer = 0
mergeTimer = 0
mergeInsTimer = 0

for x in range(30):
    print(x)
    array = Generator.generateRandomNumbers(10000, 1, 100000)

    start = time.clock()
    quickSortHybrid(array)
    quickInsTimer += time.clock() - start

    start = time.clock()
    quickSort(array)
    quickTimer += time.clock() - start

    start = time.clock()
    mergeSort(array)
    mergeTimer += time.clock() - start

    start = time.clock()
    mergeSortHybrid(array)
    mergeInsTimer += time.clock() - start

print("Quick sort ", quickTimer)
print("Quick sort + insertion sort ", quickInsTimer)
print("Merge sort ", mergeTimer)
print("Merge sort + insertion sort ", mergeInsTimer)