import heapq

class Node():
    def __init__(self):
        self.done = False
        self.cost = -1
        self.edge = []



N,M = map(int,input().split())

node = []

for _ in range(N):
    node.append(Node())

for _ in range(M):
    A,B,C = map(int,input().split())
    A -= 1
    B -= 1
    node[A].edge.append([C,B])
    node[B].edge.append([C,A])

q = [[0,0]]
heapq.heapify(q)

node[0].cost = 0
node[0].done = True

while len(q):
    doneNode = heapq.heappop(q)
    print(doneNode)

    node[doneNode[1]].done = True

    #update
    for info in node[doneNode[1]].edge:
        cost = info[0] + node[doneNode[1]].cost
        to = info[1]

        if node[to].cost < 0 or cost < node[to].cost:
            node[to].cost = cost
        
        if not node[to].done:
            for edge in node[to].edge:
                heapq.heappush(q, edge)
        
    
    print(q)



