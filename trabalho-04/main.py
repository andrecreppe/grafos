import os
import Graph as gh

# ================================================================= #

# ENTREGA PADRÃO = ARVORE GERADORA MINIMA
# ENTREGA VIP = QUALQUER BUSCA (DJIKSTRA)


## Load Grpah Info ##

v, a = input().split()

## Populate the Graph with data ##

graph = gh.Graph(v = int(v))

for i in range(int(a)):
    
    u, v, w = input().split()

    graph.addEdge(int(u), int(v), int(w))

## Goal Input ##

dest = input()

## PROBLEM BELOW ##

graph.printGraph()