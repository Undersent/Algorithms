
import matplotlib.pyplot as plt
import random

import networkx as nx
"""
Gr = nx.Graph()
Gr.add_edge(0,1)
Gr.add_edge(1,2)
Gr.add_edge(2,3)
print(nx.is_connected(Gr))
Gr.remove_edge(1,2)
print(nx.is_connected(Gr))
Gr.add_edge(0,3)
print(nx.is_connected(Gr))
"""
weight_to_split = 0.95
number_Of_nodes = 19 # =20
sum_of_Disconnection = 0
number_of_intervals = 10000

def createNewGraph(G):
    G.clear()
    for i in range(number_Of_nodes):
        G.add_edge(i,i+1,weight=weight_to_split)


G = nx.MultiGraph()
createNewGraph(G)



for i in range(number_of_intervals):
    #print (chance)
    for j in range(number_Of_nodes):
        chance = random.randint(0, 100)
        #print(i)
        if chance > weight_to_split * 100:
            G.remove_edge(j, j+1)
    if not nx.is_connected(G):
        sum_of_Disconnection += 1
    createNewGraph(G)

"""elarge=[(u,v) for (u,v,d) in G.edges(data=True) ]
pos=nx.spring_layout(G) # positions for all nodes
# nodes
nx.draw_networkx_nodes(G,pos,node_size=700)
# edges
nx.draw_networkx_edges(G,pos,edgelist=elarge,
                    width=6)
# labels
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')

plt.axis('off')
#plt.savefig("weighted_graph.png") # save as png
plt.show() # display"""
print("szansa że graf o 20 wierzcholkach z krawedziami o wagach 0,95 bedzie rozspojniony ",
      sum_of_Disconnection/number_of_intervals*100)

#Jak zmieni się niezawodność tej sieci po dodaniu krawędzi e(1,20) takiej, że h(e(1,20))=0.95

sum_of_Disconnection=0
createNewGraph(G)
G.add_edge(0, 19, weight=weight_to_split)

for i in range(number_of_intervals):
    #print (chance)
    for j in range(number_Of_nodes):
        chance = random.randint(0, 100)
        #print(i)
        if chance > weight_to_split * 100:
            G.remove_edge(j, j+1)
    #dodatkowe sprawdzenie dla 0-19
    chance = random.randint(0, 100)
    if chance > weight_to_split * 100:
        G.remove_edge(0, 19)
    if not nx.is_connected(G):
        sum_of_Disconnection += 1
    createNewGraph(G)
    G.add_edge(0, 19, weight=weight_to_split)

print("szansa że graf o 20 wierzcholkach z krawedziami o wagach 0,95 bedzie rozspojniony"
      "(z dodatkowa krawedzia 0-19 o wadze 0.95) ",
      sum_of_Disconnection/number_of_intervals*100)


#A jak zmieni się niezawodność tej sieci gdy dodatkowo dodamy jeszcze krawędzie
#e(1,10) oraz e(5,15) takie, że: h(e(1,10))=0.8, a h(e(5,15))=0.7.

sum_of_Disconnection=0
createNewGraph(G)
G.add_edge(0, 19, weight=weight_to_split)
G.add_edge(0, 10, weight=0.8)
G.add_edge(4,14, weight = 0.7)

for i in range(number_of_intervals):
    #print (chance)
    for j in range(number_Of_nodes):
        chance = random.randint(0, 100)
        #print(i)
        if chance > weight_to_split * 100:
            G.remove_edge(j, j+1)
    #dodatkowe sprawdzenie dla 0-19 i reszty
    chance = random.randint(0, 100)
    if chance > weight_to_split * 100:
        G.remove_edge(0, 19)
    chance = random.randint(0, 100)
    if chance > 0.8 * 100:
        G.remove_edge(0, 10)
    chance = random.randint(0, 100)
    if chance > 0.7 * 100:
        G.remove_edge(4, 14)

    if not nx.is_connected(G):
        sum_of_Disconnection += 1
    createNewGraph(G)
    G.add_edge(0, 19, weight=weight_to_split)
    G.add_edge(0, 10, weight=0.8)
    G.add_edge(4, 14, weight=0.7)

print("szansa że graf o 20 wierzcholkach z krawedziami o wagach 0,95 bedzie rozspojniony"
      "(z dodatkowa krawedzia 0-19 o wadze 0.95)\n "
      "e(0,9) oraz e(4,14) takie, że: h(e(0,9))=0.8, a h(e(4,14))=0.7 ",
      sum_of_Disconnection/number_of_intervals*100)

#A jak zmieni się niezawodność tej sieci gdy dodatkowo
# dodamy jeszcze 4 krawedzie pomiedzy losowymi wierzchołkami o h=0.4.

sum_of_Disconnection=0
createNewGraph(G)

G.add_edge(0, 19, weight=weight_to_split)
G.add_edge(0, 10, weight=0.8)
G.add_edge(4,14, weight = 0.7)
newEdge1=random.randint(0,19)
newEdge2=random.randint(0,19)
newEdge3=random.randint(0,19)
newEdge4=random.randint(0,19)
newEdge5=random.randint(0,19)
newEdge6=random.randint(0,19)
newEdge7=random.randint(0,19)
newEdge8=random.randint(0,19)

for i in range(number_of_intervals):
    #print (chance)
    for j in range(number_Of_nodes):
        chance = random.randint(0, 100)
        #print(i)
        if chance > weight_to_split * 100:
            G.remove_edge(j, j+1)
    #dodatkowe sprawdzenie dla 0-19 i reszty
    chance = random.randint(0, 100)
    if chance > weight_to_split * 100:
        G.remove_edge(0, 19)
    chance = random.randint(0, 100)
    if chance > 0.8 * 100:
        G.remove_edge(0, 10)
    chance = random.randint(0, 100)
    if chance > 0.7 * 100:
        G.remove_edge(4, 14)

    chance = random.randint(0, 100)
    if chance > 0.4 * 100:
        G.add_edge(newEdge1, newEdge2)
    chance = random.randint(0, 100)
    if chance > 0.4 * 100:
        G.add_edge(newEdge3, newEdge4)
    chance = random.randint(0, 100)
    if chance > 0.4 * 100:
        G.add_edge(newEdge5, newEdge6)
    chance = random.randint(0, 100)
    if chance > 0.4 * 100:
        G.add_edge(newEdge7, newEdge8)

    if not nx.is_connected(G):
        sum_of_Disconnection += 1
    createNewGraph(G)
    G.add_edge(0, 19, weight=weight_to_split)
    G.add_edge(0, 10, weight=0.8)
    G.add_edge(4, 14, weight=0.7)
    newEdge1 = random.randint(0, 20)
    newEdge2 = random.randint(0, 20)
    newEdge3 = random.randint(0, 20)
    newEdge4 = random.randint(0, 20)
    newEdge5 = random.randint(0, 20)
    newEdge6 = random.randint(0, 20)
    newEdge7 = random.randint(0, 20)
    newEdge8 = random.randint(0, 20)

print("szansa że graf o 20 wierzcholkach z krawedziami o wagach 0,95 bedzie rozspojniony"
      "(z dodatkowa krawedzia 0-19 o wadze 0.95)\n "
      "e(0,9) oraz e(4,14) takie, że: h(e(0,9))=0.8, a h(e(4,14))=0.7 \n"
      "oraz 4 losowymi krawedziami o h=0.4",
      sum_of_Disconnection / number_of_intervals * 100)

nx.draw(G)
plt.show()