from queue import PriorityQueue

class Graph:
    def __init__(self, v):
        self.size = v
        self.graph = [[] for _ in range(v)]         # graph of lists
        
    def addEdge(self, u, v, w):
        if v not in map(lambda x: x[0] ,self.graph[u]):
            self.graph[u].append((v, w))
        
        if u not in map(lambda x: x[0] ,self.graph[v]):
            self.graph[v].append((u, w))
        
    def printGraph(self): # for test pourposes
        printString = ""
        
        for i, u in enumerate(self.graph):
            printString += f"V[{i}]: "
            for v, w in u:
                printString += f"({v}, {w}); "
            printString += "\n"
        
        print('Graph (List Representation):')
        print(printString)


def generateMST(graph: Graph):

    parents = [(-1,-1) for _ in range(graph.size)]
    priority_queue = PriorityQueue()
    in_tree = [False] * graph.size

    priority_queue.put((0,0,-1))

    while not priority_queue.empty():
        
        weight, current, parent = priority_queue.get()
        
        if in_tree[current]:
            continue

        in_tree[current] = True
        parents[current] = (parent, weight)

        for child, weight in graph.graph[current]:
            
            if not in_tree[child]:
                priority_queue.put((weight, child, current))
            

    #Create a Graph to represent the generated tree
    # new_graph = Graph(graph.size)
    # for i in range(graph.size):
    #     if parents[i][0] != -1:
    #         new_graph.addEdge(i, parents[i][0], parents[i][1])

    print(parents)

    cost = sum(map(lambda x: x[1], parents))

    return cost