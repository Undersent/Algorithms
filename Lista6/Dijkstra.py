from pythonds.graphs import  Graph
from Lista6 import Queue
import sys

def dijkstra(aGraph,start):
    pqBH = Queue.BinHeap()
    start.setDistance(0)
    for v in aGraph:
        pqBH.insert([v.getDistance(),v])
    while not pqBH.currentSize == 0 :
        graph = pqBH.delMin()
        currentVert = graph[1]
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                pqBH.decreaseKeyByObject(newDist, [newDist,nextVert])


def shortest(v, path,weights):
    #make shortest path from v.previous
    if v.getPred():
        path.append(v.getPred().getId())
        #print(v.getPred().getId())
        weights.append(v.getDistance())
        shortest(v.getPred(), path, weights)
    return



g = Graph()
with open('input2Dijkstra.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [float(i) for i in line]
            polyShape.append(line)
print(polyShape)
i=0
for i in range(0,int(polyShape[0][0])):
    g.addVertex(str(i))

wantToFind=None
k=0
for line in polyShape:
    print(line)
    if(k==len(polyShape)-1):
        wantToFind=line[0]
        break
    if(k>=2):
        g.addEdge(str(line[0]),str(line[1]),line[2])
        print(line[0],line[1],line[2])
        k+=1

    if (k <2):
        k += 1



"""g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")


g.addEdge("A", "B", 2)
g.addEdge("A", "C", 3)
g.addEdge("B", "C", 1)
g.addEdge("B", "D", 1)
g.addEdge("B", "E", 4)
g.addEdge("C", "F", 5)
g.addEdge("E", "F", 1)
g.addEdge("F", "G", 1)"""


print('Graph data:')
for v in g:
    for w in v.getConnections():
        vid = v.getId()
        wid = w.getId()
        print(vid," ", wid, " ", v.getWeight(w))

dijkstra(g, g.getVertex(str(wantToFind)))

for t in g.getVertices():

    target = g.getVertex(t)
    path = [t]
    weights=[]
    to=str(wantToFind)
    shortest(target, path, weights)
    print('The shortest path to ', t ," from ",wantToFind," ", path[::-1], weights[::-1])
