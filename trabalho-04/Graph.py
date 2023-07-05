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


def generateMGT(graph: Graph):
   return []