import random
import time
def generateRandomNumbers(size, min, max):
    #start = time.clock()
    array = []
    for x in range (0, size):
        a = random.randint(min, max)
        b = random.randint(min, max)
        c = random.randint(min, max)
        array.append(int((a+b+c)/3))
   # print(time.clock() - start)
    return array

def generateSortedNumbers(size, min, max):
    array = generateRandomNumbers(size, min, max)
    array.sort(reverse=True)
    return array

def generateWORepetitions(size, min, max):
    array = random.sample(range(min, max), size)
    return array


def generateWORepetitionsReverse(size, min, max):
    array = random.sample(range(min, max), size)
    array.sort(reverse=True)
    return array
