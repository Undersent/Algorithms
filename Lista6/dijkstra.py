from pythonds.graphs import  Graph, Vertex
import heapq
from Lista6.BinaryHeap import PriorityQueue
"""def dijkstra(aGraph, start, target):
    print('''Dijkstra's shortest path''')
    # Set the distance for the start node to zero
    start.setDistance(0)
    pq = PriorityQueue()
    # Put tuple pair into the priority queue
    #unvisited_queue = ([(v.getDistance(), v) for v in aGraph])
    #unvisited_queue = heapq.heapify([(v.getDistance(), v) for v in aGraph])

    #pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    #heapq.heapify(unvisited_queue)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])
    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        uv = pq.delMin()
        current = uv[1]
        current.set_visited()

        # for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)

            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                % (current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                % (current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

if __name__ == '__main__':
    last=None
    g = Graph()
    with open('inputDijkstra.txt') as f:
        polyShape = []
        for line in f:
            line = line.split()  # to deal with blank
            if line:  # lines (ie skip them)
                line = [int(i) for i in line]
                polyShape.append(line)
    print(polyShape)
    i = 0
    for i in range(0, polyShape[0][0]):
        g.addVertex(str(i))
        last = str(i)
    wantToFind = None
    k = 0
    for line in polyShape:
        print(line)
        if (k == len(polyShape) - 1):
            wantToFind = line[0]
            break
        if (k >= 2):
            g.addEdge(str(line[0]), str(line[1]), line[2])
            print(line[0], line[1], line[2])
            k += 1

        if (k < 2):
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
            print(vid, " ", wid, " ", v.getWeight(w))

    dijkstra(g, g.getVertex('0'), last)

    for t in g.getVertices():
        target = g.getVertex(t)
        path = [t]
        weights = []
        to = str(wantToFind)
        shortest(target, path, weights)
        print('The shortest path for ', t, " ", path[::-1], weights[::-1])