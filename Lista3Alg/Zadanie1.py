global comparisonsRadix
# Radix sort for numbers in base 10
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
            #print (buckets)  #Here are our digits
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array


import numpy
import pylab
import math
import random

def randomArray(length, maxInt, repetitions = 1):
    if repetitions == 1:
        array = (numpy.random.randint(1, maxInt, length))
    if repetitions == 2:
        array = (numpy.random.randint(1, maxInt, length))
    return list(array)

def sortedArray(length, maxInt, repetitions =1):
    if repetitions == 1:
        array = (numpy.random.randint(1, maxInt, length))
        array = (numpy.sort(array))
    if repetitions == 2:
        array = random.sample(range(1, maxInt), length)
        array = (numpy.sort(array))
    return list(numpy.flipud(array))


class TestAlg:
    def __init__(self, repeat=5, maxElems=1000, step=100, maxInt=100):
        self.maxInt = maxInt
        self.repeat = repeat
        self.maxElems = maxElems
        self.step = step

    def drawComparisonsSorted(self):
        results = []
        global comparisonsRadix
        for k in range(100,self.maxElems, self.step):
            comparedTimes = 0
            for i in range(0, self.repeat):
                a = sortedArray(k, self.maxInt);
                radixSortNumbers(a)
                comparedTimes+= comparisonsRadix
        #print (comparedTimes/self.repeat)
            results.append(comparedTimes/self.repeat)
        pylab.plot(results)
        pylab.show()








Test = TestAlg()
Test.drawComparisonsSorted()




#  Statement:
#  Given a disordered list of integers, rearrange them in natural order.
#
#  Sample Input: [18,5,100,3,1,19,6,0,7,4,2]
#
#  Sample Output: [0,1,2,3,4,5,6,7,18,19,100]
#
#  Time Complexity of Solution:
#  Best Case O(kn); Average Case O(kn); Worst Case O(kn),
#  where k is the length of the longest number and n is the
#  size of the input array.
#
#  Note: if k is greater than log(n) then an nlog(n) algorithm would
#  be a better fit. In reality we can always change the radix
#  to make k less than log(n).
#
#  Approach:
#  radix sort, like counting sort and bucket sort, is an integer based
#  algorithm (i.e. the values of the input array are assumed to be
#  integers). Hence radix sort is among the fastest sorting algorithms
#  around, in theory. The particular distinction for radix sort is
#  that it creates a bucket for each cipher (i.e. digit); as such,
#  similar to bucket sort, each bucket in radix sort must be a
#  growable list that may admit different keys.
#
#  For decimal values, the number of buckets is 10, as the decimal
#  system has 10 numerals/cyphers (i.e. 0,1,2,3,4,5,6,7,8,9). Then
#  the keys are continuously sorted by significant digits.