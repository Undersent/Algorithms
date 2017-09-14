import matplotlib.pyplot as plt
import random

import networkx as nx


class Krawedz:
    c =0 #Wartość C - przepustowość[pakiety / s]
    a = 0   #Wartość A - faktyczna ilość przesyłanych danych[pakiety / s]
    pr = 0.95 #Prawdopodobieństwo zerwania łącza
    start = 0
    end = 0
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def setC(self, i):
        self.c = i

    def setA(self, i):
        self.a = i

    def setPr(self, i):
        self.pr = i

    def getC(self):
        return self.c;

    def getPr(self):
        return self.pr;

    def getA(self):
        return self.a;


def createNewGraph(G):
    G.clear()
    for i in range(number_Of_nodes):
        G.add_node(i)
    for i in range(number_Of_nodes-1):
        G.add_edge(i,i+1,weight=0, C = 100, A = 0) #WEIGHT - A
        Krawedz(i,i+1)

G=nx.Graph()
number_Of_nodes = 10
weight_to_split = 0.95
createNewGraph(G)

G.add_edge(0, 9, weight=0)
Krawedz(0,9)
G.add_edge(1,7, weight= 0)
Krawedz(1,7)
print(nx.shortest_path(G, source=1, target=7))
nx.draw(G)
#plt.show()

sizeOfMatrix=10
c=10
w, h = 10, 10;
matrix = [[0 for x in range(w)] for y in range(h)]


for i in range(sizeOfMatrix):
    for j in range(sizeOfMatrix):
        matrix[i][j]=c
        if(i==j):
            matrix[i][j] = 0
#znajodowanie funkcji a dla każdej krawędzi + oblicznie gg




gg = 0
index = 0
l=1

for i in range(sizeOfMatrix):
    for j in range(sizeOfMatrix):
        gg += matrix[i][j]
        lista = nx.shortest_path(G, source=i, target=j)
        for k in range(len(lista)):
            print(matrix[i][j])
            data = G[1][2]
            print(data)
#            data += matrix[i][j]
            G[k][l]['A'] = 11
            l += 1

"""       // znajodowanie funkcji a dla każdej krawędzi + oblicznie gg
        int gg = 0;

        for (i=1; i<=v; i++) {
            for (j=1; j<=v; j++) {
                gg += n[i-1][j-1];
                //szukanie najkrótszej ścieżki dla n(i,j) i zwiększanie a na krawędzi o n(i,j)
                List<Krawedz> lista = DijkstraShortestPath.findPathBetween(g, i, j);

                for(Krawedz kr: lista) {
                    kr.setA(kr.getA()+n[i-1][j-1]);
                }
            }
        }"""



