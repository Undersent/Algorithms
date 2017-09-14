class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def isEmpty(self):
        if(self.currentSize == 0):
            return True
        else:
            return False

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i][0] < self.heapList[i // 2][0]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i][0] > self.heapList[mc][0]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2][0] < self.heapList[i*2+1][0]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval


    def parent(self, i):
        return (i ) // 2

    #bh.decreaseKey(2, [7, [1, 1, 4]])
    # Decrease value of key at index 'i' to new_val
    def decreaseKey(self, i, new_val):
        #print(self.heapList[self.parent(i)][1],"aa")
        self.heapList[i][1]  = new_val[1]
        while(i != 0 and self.heapList[self.parent(i)][0] > self.heapList[i][0]):
            self.heapList[i][0] , self.heapList[self.parent(i)][0] = (
            self.heapList[self.parent(i)][0], self.heapList[i][0])


    def decreaseKeyByObject(self, weight, newval):
        #self.heapList.pop(0)
        #print(self.heapList)
        #print(newval)
        curval = None
        index=0
        for item in self.heapList:

            if item == 0:
                continue
            index += 1
            if(item[1] == newval[1]):
                curval = item
                break


        #print(curval)
        self.heapList[index] = newval
        if newval[0] > curval[0]:
            self.percDown(index)
        # decrease key
        elif newval[0] < curval[0]:
            self.percUp(index)
        return


tab = [0]
tab.append([1,[2,4,1]])
tab.append([6,[2,6,6]])
tab.append([2,[1,1,2]])

print(tab[0]) #2
print(tab[1][1])  #3
print(tab[1][0])
print("#####")

bh = BinHeap()
bh.insert([1,[2,3,2]])
bh.insert([2,[2,3,4]])
bh.insert([3,[2,3,8]])
bh.insert([4,[2,3,1]])
bh.insert([5,[2,3,2]])
bh.insert([6,[2,3,4]])
bh.insert([7,[2,3,8]])
bh.insert([8,[2,3,1]])
bh.insert([9,[2,3,1]])
bh.insert([10,[2,3,1]])
bh.decreaseKey(8,[8,[1,1,4]])
print(bh.currentSize)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())




#bh.buildHeap([9,5,6,2,3,11,12,14]) #2,3,5,6,9
#bh.decreaseKey(2,10)  #2 5 6 9 10"""




"""class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def isEmpty(self):
        if(self.currentSize == 0):
            return True
        else:
            return False

    def percUp(self,i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1


    # runs in log(n) time
    def decreaseKey(self, pos, newval):
        '''Replace the key at node `node` in the max-heap `A` by `newval`.
        The heap size does not change.'''
        curval = self.heapList[pos]
        self.heapList[pos] = newval
        if newval > curval:
            self.percDown(pos)
        # decrease key
        elif newval < curval:
            self.percUp(pos)
        return

bh = BinHeap()
bh.buildHeap([9,5,6,2,3,11,12,14]) #2,3,5,6,9
bh.decreaseKey(2,10)  #2 5 6 9 10"""




