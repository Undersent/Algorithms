"""import sys
from Lista6 import Queue
class MST:
    def __init__(self, vertices):
        self.V = vertices # number of vertices
        self.prioQueue = Queue.BinHeap()
        # a utulity function to find the vertex with minimum key
        # value, from the set of vertices not yet included in MST

    def minKey(self, key, mstSet):

        min = sys.maxsize
        min_index = -1

        for i in range (0, self.V):
            if(mstSet[i] == False and key[i] < min):
                min = key[i]
                min_index = i

        return min_index


    # print constructed MST stored in parent[]
    def printMST(self,parent, n, graph):
        minSpanTreeValue = 0
        print("Edge     Weight")
        for i in range(0, self.V):
            print(parent[i]," - ", i,"    ",
                               graph[i][parent[i]])
            minSpanTreeValue += graph[i][parent[i]]
        print("Minimal spanning tree ", minSpanTreeValue)


    # function to construct and peint MST for graph represented
    #using adjacency matrix representation
    def primMST(self, graph):
        #array to store constructed MST
        parent = []
        #key values used to pick minimum weight in cut
        key = []
        # to represent set of vertices not yet included in MST
        mstSet = []

        for i in range(0, self.V):
            #key[i] = sys.maxsize
            key.append(sys.maxsize)
            parent.append(None)
            mstSet.append(False)
            self.prioQueue.insert([key[i],mstSet])

        # always include fisrt vertex in MST
        key[0] = 0
        parent[0] = -1

        for count in range(0, self.V-1):
            #pick the minimum key vertex from set of vertices
            #not yet included in MST
            u = self.minKey(key, mstSet)
            print("U: ", u , " a z kolejki ", self.prioQueue.delMin())
            mstSet[u] = True

            #update key value and parent index of the adjacent
            #vertices of the picked vertex. COnsider only those
            # vertices which are not yet included in MST
            for v in range(0,self.V):
                #graph[u][v] is non zero only for adjacent vertices of m
                #mstSet[v] is false for vertices not yet included in MST
                #Update the key only if graph[u][v] is smaller than key[v]
                #print(graph[u][v],"a")
                if(graph[u][v]!=0 and mstSet[v] == False
                   and graph[u][v] < key[v]):
                    parent[v] = u
                    key[v] = graph[u][v]


        self.printMST(parent,self.V, graph)

t = MST(5)

graph = [[0,2,0,6,0],
         [2,0,3,8,5],
         [0,3,0,0,7],
         [6,8,0,0,9],
         [0,5,7,8,0],
         ]
t.primMST(graph)
"""

imaport sys
from Lista6 import Queue
class MST:
    def __init__(self, vertices):
        self.V = vertices # number of vertices
        # a utulity function to find the vertex with minimum key
        # value, from the set of vertices not yet included in MST

    def minKey(self, key, mstSet):

        min = sys.maxsize
        min_index = -1

        for i in range (0, self.V):
            if(mstSet[i] == False and key[i] < min):
                min = key[i]
                min_index = i

        return min_index
    # print constructed MST stored in parent[]
    def printMST(self,parent, n, graph):
        minSpanTreeValue = 0
        print("Edge     Weight")
        for i in range(0, self.V):
            print(parent[i]," - ", i,"    ",
                               graph[i][parent[i]])
            minSpanTreeValue += graph[i][parent[i]]
        print("Minimal spanning tree ", minSpanTreeValue)


    # function to construct and peint MST for graph represented
    #using adjacency matrix representation
    def primMST(self, graph):
        #array to store constructed MST
        parent = []
        #key values used to pick minimum weight in cut
        key = []
        # to represent set of vertices not yet included in MST
        mstSet = []
        prioQueue = Queue.BinHeap()
        for i in range(0, self.V):
            #key[i] = sys.maxsize
            key.append(sys.maxsize)
            parent.append(None)
            mstSet.append(False)


        # always include fisrt vertex in MST
        key[0] = 0
        parent[0] = -1

        for count in range(0, self.V-1):
            #pick the minimum key vertex from set of vertices
            #not yet included in MST
            u = self.minKey(key, mstSet)

            mstSet[u] = True

            #update key value and parent index of the adjacent
            #vertices of the picked vertex. COnsider only those
            # vertices which are not yet included i MST
            for v in range(0,self.V):
                #graph[u][v] is non zero only for adjacent vertices of m
                #mstSet[v] is false for vertices not yet included in MST
                #Update the key only if graph[u][v] is smaller than key[v]
                if(graph[u][v]!=0 and mstSet[v] == False
                   and graph[u][v] < key[v]):
                    parent[v] = u
                    key[v] = graph[u][v]


        self.printMST(parent,self.V, graph)

t = MST(5)

graph = [[0,2,0,6,0],
         [2,0,3,8,5],
         [0,3,0,0,7],
         [6,8,0,0,9],
         [0,5,7,8,0],
         ]
t.primMST(graph)
