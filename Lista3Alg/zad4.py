complexityOfQuick = []
swapsOfQuick = []
import random
import pylab

def medianOfmedians(ls):
    subs = [ls[i:i + 5] for i in range(0, len(ls), 5)]  # partition in n/5 groups of length at most 5 each
    median_ls = [sorted(sub)[len(sub) // 2] for sub in subs]
    if len(median_ls) <= 5:
        return sorted(median_ls)[len(median_ls) // 2]
    else:
        return medianOfmedians(median_ls)  # pivot is the median of medians

def quickSort(array):
    global numberOfCompQuick
    global numberOfSwapsQuick

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = medianOfmedians(array)
        #print(pivot)
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

numberOfCompQuick = 0
numberOfSwapsQuick = 0
start = 100       # minimalny rozmiar tablicy
end = 10000
step = 100
array = None


#x = [13,6,9,5,4,7,18,3,1,22,21,44,55,66,77,88,99,111,100,15,33,34,35,36,37,38]

#print(quickSort(x))


for sizeOfData in range(start,end +1, step):
    print("counting for ", sizeOfData)

    numberOfCompQuick = 0
    numberOfSwapsQuick = 0
    array = random.sample(range(1,1000000), sizeOfData)
    array.sort(reverse=True)
    quickSort(array)
    complexityOfQuick.append(numberOfCompQuick)
    swapsOfQuick.append(numberOfSwapsQuick)


pylab.plot(complexityOfQuick)
pylab.show()