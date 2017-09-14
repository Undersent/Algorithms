import pylab
import random
from lista4alg import BST
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)


mytree = BST.BinarySearchTree()
lista=[]
for i in range (1,1000,1):
    print(i)
    mytree.insert(i,i)
    #lista.append(mytree.getComparisonsOfInsert())

for i in range (1,1000,1):
    print(i)
    mytree.find(i)
    lista.append(mytree.getComparisonsOfInsert())

pylab.plot(lista)
pylab.show()

"""mytree = BST.BinarySearchTree()

lista=[]
start = 500
end = 1000
for i in range (start,end,1):
    mytree.insert(abs(start-i),abs(start-i))
    lista.append(mytree.getComparisonsOfInsert())
    mytree.insert(i, i)
    lista.append(mytree.getComparisonsOfInsert())

pylab.plot(lista)
pylab.show()"""

mytree = BST.BinarySearchTree()
lista=[]
lista1=[]
for i in range (1,10000,1):
    print(i)
    number = random.randint(1,1000000)
    lista1.append(number)
    mytree.insert(number,number)

for i in range (1,10000,1):
    number = random.randint(1,9999)
    mytree.find(lista1[number-1])
    lista.append(mytree.getComparisonsOfInsert())



pylab.plot(lista)
pylab.show()

mytree = BST.BinarySearchTree()
lista=[]
for i in range (1,10000,1):
    print(i)
    number = random.randint(1,1000000)
    mytree.insert(number,number)
    lista.append(mytree.getComparisonsOfInsert())

pylab.plot(lista)
pylab.show()