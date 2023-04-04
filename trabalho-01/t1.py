import os

class Graph:
    def __init__(self, v):
        self.size = v
        self.graph = [[] for _ in range(v)] # graph of lists
        self.graph_header = [0 for _ in range(v)]

    def addEdge(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph_header[v2] += 1
        self.graph[v2].append(v1)
        self.graph_header[v1] += 1

    def printGraph(self):
        print('Graph (List Representation):')
        for i, v in enumerate(self.graph):
            count = self.graph_header[i]
            print(f'V[{i}] = {count} --> {v}')

    def isEuler(self):
        # Theorem: If every vertex has an *even* number of connections, it has an Euler Path 
        for v_count in self.graph_header:
            if (v_count % 2) != 0:
                return False
            
        return True
    
    def findEuler(self):
        visitedEdges = [[False for _ in range(self.size)] for _ in range(self.size)] # Track visited lines
        startPos = 0

        path = self.dfs(startPos, self.graph, visitedEdges)

        return path

    def dfs(self, v0, graph, visitedEdges, path = []): # Depth-first search algorithm
        path += [v0]
        
        for v1 in graph[v0]:
            if visitedEdges[v0][v1] == False:
                visitedEdges[v0][v1] = True
                visitedEdges[v1][v0] = True

                path = self.dfs(v1, graph, visitedEdges, path)
        
        return path

# ================================================================= #

## Read the file and Grpah Info ##

here = os.path.dirname(os.path.abspath(__file__))

filename = input()
# filename = 'ex1.in'
# filename = 'ex2.in'
file = open(os.path.join(here, filename), 'r')
v, a = file.readline().split(' ')

## Populate the Graph with data ##

graph = Graph(int(v))

for i in range(int(a)):
    line = file.readline().replace('\n', '')
    v0, v1 = line.split(' ')

    graph.addEdge(int(v0), int(v1))

file.close()

# graph.printGraph()

## Check and Solve for Euler Path ##

if graph.isEuler():
    path = graph.findEuler()
    
    print('Sim')
    [print(n, end = ' ') for n in path]
else:
    print('Não')
