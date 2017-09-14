from pythonds.graphs import Graph,PriorityQueue
#from Lista6.BinaryHeap import PriorityQueue
import sys

"""global last
def prim(G,start):
    global last
    pq = PriorityQueue()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    min=0
    weights=0
    MST = []
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()
        for nextVert in currentVert.getConnections():
              newCost = currentVert.getWeight(nextVert)
              if nextVert in pq and newCost<nextVert.getDistance():
                  nextVert.setPred(currentVert)
                  nextVert.setDistance(newCost)
                  pq.decreaseKey(nextVert,newCost)
                  MST.append(nextVert)
                  for v in MST:
                      print("nv ",nextVert.getDistance())
                      print("v ",v.getDistance())
                      if(nextVert == v):

                          v=nextVert
    distance =0
    for i in MST:
        distance +=i.getDistance()
    print(distance)

def shortest(v, path,weights):
    ''' make shortest path from v.previous'''
    if v.getPred():
        path.append(v.getPred().getId())
        #print(v.getPred().getId())
        weights.append(v.getDistance())
        shortest(v.getPred(), path, weights)
    return



g = Graph()
with open('input.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            polyShape.append(line)
print(polyShape)
i=0
for i in range(0,polyShape[0][0]):
    g.addVertex(str(i))

wantToFind=None
k=0
for line in polyShape:

    if(k>=2):
        g.addEdge(str(line[0]),str(line[1]),line[2])
        print(line[0],line[1],line[2])
        k+=1

    if (k <2):
        k += 1


print('Graph data:')
for v in g:
    for w in v.getConnections():
        vid = v.getId()
        wid = w.getId()
        print(vid," ", wid, " ", v.getWeight(w))

prim(g, g.getVertex('0'))

for t in g.getVertices():

    target = g.getVertex(t)
    path = [t]
    weights=[]
    to=str(wantToFind)
    shortest(target, path, weights)
    print('The shortest path for ', t ," ", path[::-1], weights[::-1])


