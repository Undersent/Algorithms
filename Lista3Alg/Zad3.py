global comparisons
import random

import numpy
import pylab


def select(ls, i):
    global comparisons
    subs = [ls[i:i + 5] for i in range(0, len(ls), 5)]  # partition in n/5 groups of length at most 5 each
    #print (subs)
    median_ls = [sorted(sub)[len(sub) // 2] for sub in subs]
    #comparisons += 1
    if len(median_ls) <= 5 :
        #print("median ",median_ls)

        pivot = sorted(median_ls)[len(median_ls) // 2]
    else:
        pivot = select(median_ls, len(median_ls) // 2)  # pivot is the median of medians

    # pivot = median(median_ls)
    # partition array around the pivot
    low = [j for j in ls if j < pivot ]
    comparisons += len(ls)
    high = [j for j in ls if j > pivot]

    k = len(low)
    #comparisons += 1
    if i < k:
        return select(low, i)
    elif i > k:
        return select(high, i - k - 1)
    else:
        return pivot


class TestAlg:
    def __init__(self, repeat=1, maxElems=10000, step=100, maxInt=100000):
        self.maxInt = maxInt
        self.repeat = repeat
        self.maxElems = maxElems
        self.step = step

    def drawComparisonsSorted(self):
        results = []

        global comparisons
        comparisons=0
        for k in range(100,self.maxElems, self.step):
            number = numpy.random.randint(0, k)
            comparedTimes = 0
            for i in range(0, self.repeat):
                a = random.sample(range(1,self.maxInt), k)
                #a.sort(reverse=True)
                select(a, number)
                comparedTimes+= comparisons
                comparisons=0
        #print (comparedTimes/self.repeat)
            results.append(comparedTimes/self.repeat)
        #pylab.plot(results)
        #pylab.show()
        return results

Test = TestAlg()
Test.drawComparisonsSorted()

#x=random.sample(range(1, 1000000), 100000)
# foto 1 repeat=50, maxElems=10000, step=100, maxInt=100000): unsorted
#   foto 2 repeat=50, maxElems=10000, step=100, maxInt=100000 reverse
