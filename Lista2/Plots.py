with open("complexityOfInsertion", 'r') as f:
    arrayIns = [int(line.rstrip('\n')) for line in f]

with open("swapsOfInsertion", 'r') as f:
    arrayInsSwap = [int(line.rstrip('\n')) for line in f]

with open("complexityOfQuick", 'r') as f:
    arrayQuick = [int(line.rstrip('\n')) for line in f]

with open("swapsOfQuick", 'r') as f:
    arrayQuickSwap = [int(line.rstrip('\n')) for line in f]

with open("complexityOfMerge", 'r') as f:
    arrayMerge = [int(line.rstrip('\n')) for line in f]

with open("swapsOfMerge", 'r') as f:
    arrayMergeSwap = [int(line.rstrip('\n')) for line in f]

import matplotlib.pyplot as plt

plt.title('Insertion Comp')
plt.plot(arrayIns)
plt.ylabel('Insertion')
plt.show()

plt.title('Insertion Swap')
plt.plot(arrayInsSwap)
plt.ylabel('InsertionSwap')
plt.show()

plt.title('Quick comp')
plt.plot(arrayQuick)
plt.ylabel('Quick')
plt.show()


plt.title('Quick swap')
plt.plot(arrayQuickSwap)
plt.ylabel('QuickSwap')
plt.show()

plt.title('Merge comp')
plt.plot(arrayMerge)
plt.ylabel('Merge')
plt.show()

plt.title('merge swap')
plt.plot(arrayMergeSwap)
plt.ylabel('MergeSwap')
plt.show()

plt.title(' quick - blue, merge - green')
#plt.plot( arrayQuick, 'bs', arrayMerge, 'g^')
plt.plot(arrayQuick, 'bs', arrayMerge, 'g^' )
plt.show()
plt.title(' quickSwap - blue, mergeSwap - green')
plt.plot(arrayQuickSwap, 'bs', arrayMergeSwap, 'g^' )
plt.show()