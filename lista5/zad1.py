global comparisons

global comparisonsRandSelect
global results
from Lista2 import Generator

class Alg:
    def __init__(self, repeat=30, maxElems=3000, step=50, maxInt=100000):
        self.maxInt = maxInt
        self.repeat = repeat
        self.maxElems = maxElems
        self.step = step

    def drawComparisonsSorted(self):
        global results
        results = []

        global comparisonsRandSelect
        comparisonsRandSelect=0
        for k in range(1000,self.maxElems, self.step):
            number = numpy.random.randint(0, k)
            comparedTimes = 0
            print(k)
            for i in range(0, self.repeat):
                a = Generator.generateRandomNumbers(k, 0, self.maxInt);
                a.sort(reverse=True)
                #a = random.sample(range(0, self.maxInt), k)
                RSelect(a, number)
                comparedTimes+= comparisonsRandSelect
                comparisonsRandSelect=0
        #print (comparedTimes/self.repeat)
            results.append(comparedTimes/self.repeat)
        return results

import numpy
def partition(x, pivot_index=0):
    i = 0
    global comparisonsRandSelect

    #print("tablica ", x)
    #print("pivot ", pivot_index)
    if pivot_index != 0: x[0], x[pivot_index] = x[pivot_index], x[0]
    for j in range(len(x) - 1):
        if x[j + 1] < x[0]:
            x[j + 1], x[i + 1] = x[i + 1], x[j + 1]
            comparisonsRandSelect+=1
            i += 1

    x[0], x[i] = x[i], x[0]
    return x, i

from random import randrange
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
    def __init__(self, repeat=1, maxElems=3000, step=50, maxInt=100000):
        self.maxInt = maxInt
        self.repeat = repeat
        self.maxElems = maxElems
        self.step = step

    def drawComparisonsSorted(self):
        results = []

        global comparisons
        comparisons=0
        for k in range(1000,self.maxElems, self.step):
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


class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent


    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self





class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
        self.valueOfRoot = None

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def getComparisonsOfInsert(self):
        global comparisons
        return comparisons

    def insert(self, key, val):
        global comparisons
        comparisons = 0
        if self.root:
            self._insert(key, val, self.root)
        else:
            self.root = TreeNode(key,val)
            self.valueOfRoot=key
        self.size = self.size + 1

    def _insert(self, key, val, currentNode):
        global comparisons
        if key < currentNode.key:
            comparisons +=1
            if currentNode.hasLeftChild():
                   self._insert(key, val, currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            comparisons += 1
            if currentNode.hasRightChild():
                   self._insert(key, val, currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)

    def __setitem__(self,k,v):
       self.insert(k, v)

    def get(self,key):
       global comparisons
       comparisons = 0
       if self.root:
           res = self._get(key,self.root)
           if res:
                  return res.payload
           else:
                  return None
       else:
           return None

    def getNode(self,key):
        global comparisons
        comparisons = 0
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
       global comparisons
       if not currentNode:
           return None
       elif currentNode.key == key:

           return currentNode
       elif key < currentNode.key:
           comparisons += 1
           return self._get(key,currentNode.leftChild)
       else:
           comparisons += 1
           return self._get(key,currentNode.rightChild)

    def find(self,key):
        if self.get(key):
            return 1
        else:
            return 0

    def __getitem__(self,key):
       return self.get(key)

    def __contains__(self,key):
       if self._get(key,self.root):
           return True
       else:
           return False

    def delete(self,key):
      if self.size > 1:
         nodeToRemove = self._get(key,self.root)
         if nodeToRemove:
             self.remove(nodeToRemove)
             self.size = self.size-1
         #else:
             #raise KeyError('Error, key not in tree')
      elif self.size == 1 and self.root.key == key:
         self.root = None
         self.valueOfRoot = None
         self.size = self.size - 1
      #else:
         #raise KeyError('Error, key not in tree')

    def __delitem__(self,key):
       self.delete(key)



    def spliceOut(self):
       if self.isLeaf():
           if self.isLeftChild():
                  self.parent.leftChild = None
           else:
                  self.parent.rightChild = None
       elif self.hasAnyChildren():
           if self.hasLeftChild():
                  if self.isLeftChild():
                     self.parent.leftChild = self.leftChild
                  else:
                     self.parent.rightChild = self.leftChild
                  self.leftChild.parent = self.parent
           else:
                  if self.isLeftChild():
                     self.parent.leftChild = self.rightChild
                  else:
                     self.parent.rightChild = self.rightChild
                  self.rightChild.parent = self.parent

    def findSuccessor(self):
      succ = None
      if self.hasRightChild(): #if has right child we have to find min in right subtree
          succ = self.rightChild.findMin()
      else:
          if self.parent:
                 if self.isLeftChild(): #if is left child parents are sucessor
                     succ = self.parent
                 else: # node is right child and doesnt have right child then succesor is successor of parent
                     self.parent.rightChild = None
                     succ = self.parent.findSuccessor()
                     self.parent.rightChild = self
      return succ


    def findMin(self):
      current = self
      while current.hasLeftChild():
          current = current.leftChild
      return current

    def findMax(self):
      current = self
      while current.hasRightChild():
          current = current.RightChild
      return current

    def remove(self,currentNode):
         if currentNode.isLeaf(): #if leaf
           if currentNode == currentNode.parent.leftChild:
               currentNode.parent.leftChild = None
           else:
               currentNode.parent.rightChild = None
         elif currentNode.hasBothChildren(): #if node has two children
           succ = currentNode.findSuccessor() #have to find successor
           succ.spliceOut()
           currentNode.key = succ.key
           currentNode.payload = succ.payload

         else: # if node has one child
           if currentNode.hasLeftChild():
             if currentNode.isLeftChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.leftChild
             elif currentNode.isRightChild():
                 currentNode.leftChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.leftChild
             else: #id node is root
                 currentNode.replaceNodeData(currentNode.leftChild.key,
                                    currentNode.leftChild.payload,
                                    currentNode.leftChild.leftChild,
                                    currentNode.leftChild.rightChild)
           else:
             if currentNode.isLeftChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.leftChild = currentNode.rightChild
             elif currentNode.isRightChild():
                 currentNode.rightChild.parent = currentNode.parent
                 currentNode.parent.rightChild = currentNode.rightChild
             else: #id node is root
                 currentNode.replaceNodeData(currentNode.rightChild.key,
                                    currentNode.rightChild.payload,
                                    currentNode.rightChild.leftChild,
                                    currentNode.rightChild.rightChild)

global numbers
def inorder(node):
    global numbers
    if node:
        inorder(node.hasRightChild())
        numbers+=str(node.payload)+" "
        inorder(node.hasLeftChild())
    return numbers

def findMin(node):
  while node.hasLeftChild():
      node = node.hasLeftChild()

  return node

def findMax(current):
  while current.hasRightChild():
      current = current.hasRightChild()
  return current


def size(node):
    if (node ):
        return size(node.hasRightChild()) + 1 + size(node.hasLeftChild())
    else:
        return 0
global selectComp


#Select(i) — find the i'th smallest element stored in the tree
#Rank(x) – find the rank of element x in the tree, i.e. its index in the sorted list of elements of the tree
def OSSelect(node,i):
    if node:
        k = size(node.hasLeftChild())+1
        global selectComp
        selectComp+=1
        if i==k:
            return node
        elif i<k:
            return OSSelect(node.hasLeftChild(),i)
        else:
            return OSSelect(node.hasRightChild(), i-k)
    else:
        return None

def OSRank(node, x):
    r = size(node.hasLeftChild()) + 1
    y = x
    while y != node: #dopoki nie rowna sie root
        if y == (y.parent).hasRightChild(): #y ma prawego syna
            r = r + size((y.parent).hasLeftChild()) +1 #dajemy wielkosc lewej strony
        y=y.parent
    return r

import random
import numpy as np
import matplotlib.pyplot as plt
#mytree = BinarySearchTree()
maxSize = 3000
t = np.arange(1, maxSize, 1)
myNumbers = []


data = []
times = 30
listOfCompSelect = []
for i in range (1000,maxSize,50):
    print(i)


    selectCompFull = 0
    for k in range(0,times): #times razy wyszukuje
        mytree = BinarySearchTree()
        for j in range(0, i):  # tworze drzewo
            number = random.randint(1, 1000000)
            mytree.insert(number, number)
        selectComp=0
        OSSelect(mytree.root, random.randint(1, i))
        selectCompFull += selectComp
    data.append(i)
    listOfCompSelect.append(selectCompFull/times)

import pylab
import Lista3Alg


Testownik = Alg()
resultRand = Testownik.drawComparisonsSorted()
#pylab.plot(resultRand)
#pylab.show()
Test = TestAlg()
resultSelect = Test.drawComparisonsSorted()
#pylab.plot(resultSelect)
#pylab.plot
#pylab.show()

#pylab.plot(listOfCompSelect)
#pylab.show()
t = np.arange(1000, 3000, 50)
pylab.plot(t,resultRand,'r--',t,resultSelect,'bs', t,listOfCompSelect,'g^')
pylab.show()
#pylab.plot(results)
#pylab.show()

#plt.plot(data, resultRand, 'r--', data, resultSelect, 'bs', data, listOfCompSelect, 'g^')
#plt.show()
#pylab.plot(listOfCompSelect)
#pylab.show()

"""listOfCompSelect = []
for i in t:
    #print(i)
    selectComp=0
    #losowy = random.randint(1,maxSize)-1
    #print(losowy)
    #number = myNumbers[losowy]

    listOfCompSelect.append(selectComp)
    print(selectComp)"""


"""mytree.insert(3,3)
mytree.insert(2,2)
mytree.insert(4,4)
mytree.insert(5,5)
mytree.insert(6,6)
mytree.insert(7,7)

#print(size(mytree.root.hasLeftChild()))
#print(size(mytree.root)) #6
#print(size(mytree.getNode(4))) #4
#print(size(mytree.getNode(4).hasLeftChild())) #3
#print("oddzielenie")
#print(OSSelect(mytree.root,4).payload)

#print(mytree.getNode(4).parent.payload) # 4

#print(OSRank(mytree.root , mytree.getNode(7)))"""

