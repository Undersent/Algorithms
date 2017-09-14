from Lista6 import Queue
def shortestPath(graph, start):
    # cost, start_vertex , parent

    priorityQueue = Queue.BinHeap()
    priorityQueue.insert([0,['0',-1,0]])
    mstTree = []
    #print("abc", priorityQueue.delMin())
    # visited set
    seen = set()

    while True:
        _, info = priorityQueue.delMin()
        vertex = info[0]
        parent_vertex = info[1]
        cost = info[2]

        if vertex not in seen:
            # vertex is not in visited list , add it
            seen.add(vertex)
            mstTree.append((vertex, parent_vertex,cost))
            if len(seen) == len(graph):
                break

            #Update min heap with all adjacent vertex cost,vertex,parent
            for (next_vertex, cost_vertex) in graph[vertex].items():
                priorityQueue.insert([cost_vertex,[next_vertex, vertex, cost_vertex]])

    return mstTree



"""G = {'0': {'1':10, '2':6, '3':5},
'1': {'0':10,'3':15},
'2': {'0': 6, '3':4},
'3':{'4':105,'1':15, '2':4, '0' : 5},
'4':{'3':105}}
print(shortestPath(G, '0'))
print("length :" + str(len(G)))"""



with open('input.txt') as f:
    polyShape = []
    for line in f:
        line = line.split() # to deal with blank
        if line:            # lines (ie skip them)
            line = [i for i in line]
            polyShape.append(line)

verticles = int(polyShape[0][0])
Gx = {}

for i in range(0,verticles):
    Gx[str(i)] = None

polyShape.pop(0)
polyShape.pop(0)
#print(polyShape)
for index in range(0,verticles):
    Gy = {}
    for item in polyShape:
        if item[0] == index:
            Gy[str(item[1])] = item[2]
        if index == item[1]:
            Gy[str(item[0])] = item[2]
        #print("gy ",Gy)
    Gx[str(index)] = Gy

mst = (shortestPath(Gx, '0'))
sum =0
mst.pop(0)
for item in mst:
    sum += item[2]
    print ("From ", item[0], " To ",item[1], " weight ", item[2])
print("Minimal spanning tree ", sum)
print("length :" + str(len(Gx)-1))
#647