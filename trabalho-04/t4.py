import os

class Graph:
    def __init__(self, v):
        self.size = v
        self.graph = [[] for _ in range(v)]         # graph of lists
        self.graph_header = [0 for _ in range(v)]

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph_header[u] += 1

    def printGraph(self): # for test pourposes
        printString = ""
        
        for i, u in enumerate(self.graph):
            printString += f"V[{i}]: "
            for v, w in u:
                printString += f"({v}, {w}); "
            printString += "\n"
        
        print('Graph (List Representation):')
        print(printString)

# ================================================================= #

# ENTREGA PADRÃO = ARVORE GERADORA MINIMA
# ENTREGA VIP = QUALQUER BUSCA (DJIKSTRA)

## Read local file or execute in RunCodes enviroment ##

runcodes = False
testName = '1.in'

## Load Grpah Info ##

if runcodes:
    v, a = input().split()
else : 
  here = os.path.dirname(os.path.abspath(__file__))
  filename = os.path.join('test', testName)
  file = open(os.path.join(here, filename), 'r')
  
  v, a = file.readline().split(' ')

## Populate the Graph with data ##

graph = Graph(v = int(v))

for i in range(int(a)):
    if runcodes:
      u, v = input().split()
    else:
      line = file.readline().replace('\n', '')
      u, v, w = line.split(' ')

    graph.addEdge(int(u), int(v), int(w))

# graph.printGraph()

## Goal Input ##

if runcodes:
    dest = input()
else:
  dest = file.readline()
  file.close()

## PROBLEM BELOW ##

