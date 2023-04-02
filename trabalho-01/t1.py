class Graph:
    def __init__(self, v):
        self.size = v
        self.graph = [[] for x in range(v)]
        self.graph_header = [0 for x in range(v)]

    def addEdge(self, a, b):
        self.graph[a].append(b)
        self.graph_header[a] += 1
        self.graph[b].append(a)
        self.graph_header[b] += 1

    def printInfo(self):
        print('Graph:')
        for i, v in enumerate(self.graph):
            count = self.graph_header[i]
            print(f'V[{i}] = {count} --> {v}')

    def isEuler(self):
        # Every vertice should have an even number of connections
        for v_count in self.graph_header:
            if (v_count % 2) != 0:
                return False
            
        return True
    
    def findEuler(self):
        visitedEdges = [[False for x in range(self.size)] for y in range(self.size)] # visit matrix

        startPos = 0
        path = self.dfs(startPos, self.graph, visitedEdges, [])
        
        return path

    def dfs(self, start, graph, visitedEdges, path): # Depth-first search algorithm
        path += [start]
        
        for v in graph[start]:
            if visitedEdges[start][v] == False:
                visitedEdges[start][v] = True
                visitedEdges[v][start] = True
                
                path = self.dfs(v, graph, visitedEdges, path)
        
        return path


# =================================================================

## Read the file and Grpah Info

# filename = input()
filename = 'ex1.in'
file = open(filename, 'r')
v, a = file.readline().split(' ')

## Populate the Graph with data

graph = Graph(int(v))

for i in range(int(a)):
    line = file.readline().replace('\n', '')
    v0, v1 = line.split(' ')

    graph.addEdge(int(v0), int(v1))

file.close()

if graph.isEuler():
    print('Sim')
    print(graph.findEuler())
else:
    print('Não')
