import Graph as gh

## Load Grpah Info ##

v, a = input().split()

## Populate the Graph with Data ##

graph = gh.Graph(v = int(v))

for i in range(int(a)):
    u, v, w = input().split()
    graph.addEdge(int(u), int(v), int(w))

# graph.printGraph()

## Goal Input ##

goal = input()

## Problem Solving ##

mst_cost = gh.generateMST(graph = graph)
vip_cost = gh.dijkstraDist(graph = graph, goal = int(goal))

print(f'mst = {mst_cost}')
print(f'vip = {vip_cost}')

# if mst_cost < vip_cost:
#     print('PADRAO')
#     print(mst_cost)
# else:
#     print('VIP')
#     print(vip_cost)
