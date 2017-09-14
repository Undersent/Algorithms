global comparisons


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

"""g"lobal numbers
numbers =""
mytree = BinarySearchTree()
#mytree[3]="red"
#mytree[4]="blue"
#mytree[6]="yellow"
#mytree[2]="at"
mytree.insert(3,3)
mytree.insert(2,2)
mytree.insert(4,4)

#print(mytree.get(findMin(mytree._get(mytree.valueOfRoot,mytree.root))))
print( findMin(mytree.root).payload )
#inorder(mytree.get(3))"""


mytree = BinarySearchTree()
i=0
plik = open("input.txt")
size = plik.readline()
global numbers
numbers =""
list=[]
for line in open("input.txt") :
    list.append(str(line.rstrip())) # .rstrip() removes the line break


for text in list :
    if text.startswith("insert"):
        value = int((text.split(" ",1)[1]))
        mytree.insert(value,value)
    elif text.startswith("min"):
        if mytree.root:
            print(findMin(mytree.root).payload)
        else :
            print("")
    elif text.startswith("max"):
        if mytree.root:
            print(findMax(mytree.root).payload)
        else :
            print("")
    elif text.startswith("inorder"):
        print(inorder(mytree.root))
    elif text.startswith("delete"):
        value = int((text.split(" ",1)[1]))
        mytree.delete(value)
    elif text.startswith("find"):
        value = int((text.split(" ", 1)[1]))
        print(mytree.find(value))