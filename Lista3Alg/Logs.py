from random import randrange

global comparisonsRandSelect
import math

def radixSortNumbers(array):
    global comparisonsRadix
    comparisonsRadix = 0
    maxLen = -1
    for number in array: # Find longest number, in digits
        numLen = int(math.log10(number)) + 1
        if numLen > maxLen:
            maxLen = numLen
    buckets = [[] for i in range(0, 10)] # Buckets for each digit
    for digit in range(0, maxLen): #
        for number in array:
            buckets[number // 10**digit % 10].append(number)
            comparisonsRadix+=1
            print (buckets)  #Here are our digits
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array

x=[345,123,985,234,1111,32]
print(radixSortNumbers(x))


def partition(x, pivot_index=0):
    i = 0
    global comparisonsRandSelect

    print("tablica ", x)
    print("pivot ", pivot_index)
    if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x) - 1):
        if x[j + 1] < x[0]:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            comparisonsRandSelect+=1
            i += 1

    x[0], x[i] = x[i], x[0]
    return x, i


def RSelect(x, k):
    if len(x) == 1:
        return x[0]
    else:
        xpart = partition(x, randrange(len(x)))
        #print (xpart)
        x = xpart[0]  # partitioned array
        j = xpart[1]  # pivot index
        if j == k:
            return x[j]
        elif j > k:
            return RSelect(x[:j], k)
        else:
            k = k - j - 1
            return RSelect(x[(j + 1):], k)

global comparisonsRandSelect
comparisonsRandSelect=0
i=6
x = [13,6,9,5,4,7,18,3,1,22]
#for i in range(len(x)):
print (RSelect(x,i))
y=sorted(x)
print(y)
print (comparisonsRandSelect)


def Select(ls, i):
    '''select the ith order stat of the list ls'''
    groups = [ls[i:i + 5] for i in range(0, len(ls), 5)]  # partition in n/5 groups of length at most 5 each
    print (groups)
    median_ls = [sorted(group)[len(group) // 2] for group in groups]
    print ("mediana z list ",median_ls)
    if len(median_ls) <= 5:
        pivot = sorted(median_ls)[len(median_ls) // 2]
    else:
        print("dlugosc ",len(median_ls) // 2)
        pivot = Select(median_ls, len(median_ls) // 2)  # pivot is the median of medians
        print("pivot ", pivot)

    # pivot = median(median_ls)
    # partition array around the pivot

    low = [j for j in ls if j < pivot]
    high = [j for j in ls if j > pivot]
    #print ("low" ,low)
    #print ("high " ,high)
    k = len(low)

    if i < k:
        return Select(low, i)
    elif i > k:
        return Select(high, i - k - 1)
    else:
        return pivot

i=6
print("SELECT")
x = [13,6,9,5,4,7,18,3,1,22,21,44,55,66,77,88,99,111,100,15,33,34,35,36,37,38]

print (Select(x,i))
y=sorted(x)
print(y)