from Lista6 import Queue
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # A utility function to find set of an element i
    def find(self, parent, i):
        if parent[int(i)] == i:
            return i
        return self.find((parent), parent[int(i)])

    # A function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Attach smaller rank tree under root of high rank tree
        # (Union by Rank)
        if rank[int(xroot)] < rank[int(yroot)]:
            parent[int(xroot)] = yroot
        elif rank[int(xroot)] > rank[int(yroot)]:
            parent[int(yroot)] = xroot
        # If ranks are same, then make one as root and increment
        # its rank by one
        else:
            parent[int(yroot)] = xroot
            rank[int(xroot)] += 1


    # The main function to construct MST using Kruskal's algorithm
    def KruskalMST(self):

        # This will store the resultant MST
        resultQ = Queue.BinHeap()

        e = 0  # An index variable

        # insert into binary heap
        prioQueue = Queue.BinHeap()
        for j in range(0,len(self.graph)):
            prioQueue.insert([self.graph[j][2],self.graph[j]])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(int(self.V)):
            parent.append(node)
            rank.append(0)
            #print(parent,"a")

        # Number of edges is equal to V-1
        while e < self.V - 1:

            # Pick the smallest edge
            item = prioQueue.delMin()
            u, v, w = item[1]
            x = self.find(parent, u)
            y = self.find(parent, v)
            print(u,"  ",x,"   ",v,"   ",y)
            # If including this edge does't cause cycle, include it
            if x != y:
                e = e + 1
                #result.append([u, v, w])
                resultQ.insert([u,v,w])
                self.union(parent, rank, x, y)
                # Else discard the edge

        # print the contents of result[] to display the built MST
        print("Following are the edges in the constructed MST")
        minSpanTree = 0

        for x in range(resultQ.currentSize):
            u, v, weight = resultQ.delMin()
            print("From ", u, " To ", v, " weight ", weight)
            minSpanTree += weight
        return minSpanTree








with open('input1.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            polyShape.append(line)
print(polyShape)
k=0
for line in polyShape:
    if(k==2):
        g.addEdge(line[0],line[1],line[2])
        print(line[0],line[1],line[2])

    if (k == 1):
        k += 1
    if(k==0):
        g = Graph(line[0])
        k+=1



"""g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)"""


with open('input2.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            polyShape.append(line)
print(polyShape)

g = Graph(polyShape[0][0])

wantToFind=None
k=0
for line in polyShape:

    if(k>=2):
        g.addEdge(line[0],line[1],line[2])
        print(line[0],line[1],line[2])
        k+=1

    if (k <2):
        k += 1


print('Graph data:')
print("Minimal spanning tree ",g.KruskalMST())

