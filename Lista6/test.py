import heapq
def shortestPath(graph, start):

''' Initialized queue with start point cost is 0'''
# its a array with each element as a tuple (cost,vertex,path[])

# cost, start_vertex , parent
queue = [(0, start, -1)]
parent = []

# visited set
'''Define a set for visited list '''
seen = set()
while True:
''' each time it will return the vertex with minimum cost '''
(cost, vertex, parent_vertex) = heapq.heappop(queue)

if vertex not in seen:
''' vertex is not in visited list , add it '''
seen.add(vertex)
parent.append((vertex, parent_vertex))
if len(seen) == len(graph):
break

''' Update min heap with all adjacent vertex cost,vertex,parent '''
for (next_vertex, cost_vertex) in graph[vertex].items():
heapq.heappush(queue, (cost_vertex, next_vertex, vertex))
return parent

if __name__ == '__main__':
G = {'s': {'u':10, 'x':5},
'u': {'v':1, 'x':2},
'v': {'y':4},
'x':{'u':3, 'v':9, 'y':2},
'y':{'s':7, 'v':6}}

print(shortestPath(G, 's'))
print("length :" + str(len(G)))