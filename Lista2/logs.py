def insertionSort(array):

    for index in range(1,len(array)):
        curr = array[index]
        position = index
        print("log for insertionSort:", array)
        while position > 0 and array[position-1] > curr:

            array[position] = array[position-1]
            position = position - 1

        array[position] = curr


    return array



def quickSort(array):


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

        print("log for quickSort: less", less," equal ", equal," greater ", greater, " aray ", array)

        return quickSort(less)+equal+quickSort(greater)

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
    print("log for merge sort ", c)
    return c

# Code for merge sort

def mergeSort(array):


    if len(array) == 0 or len(array) == 1:
        return array
    else:
        middle = int(len(array)/2)
        a = mergeSort(array[:middle])
        b = mergeSort(array[middle:])
        print("log for merge sort ", a,"  ", b)
        return merge(a,b)




l=[4,6,2,8,9,11,0,2]
print(insertionSort(l))
print(quickSort(l))
print(mergeSort(l))

