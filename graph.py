import collections, heapq

def dfs(edges):
    # recursive
    graph = collections.defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def helper(node, target, visited):
        if node not in visited:
            if node == target:
                return True
            visited.add(node)
            for nei in graph[node]:
                # Don't have to check if in visited because I check at begginning
                if helper(nei, target, visited):
                    return True
        return False
    
    visited = set()
    return helper(start, target, visited)

def dfs(edges):
    # iterative
    graph = collections.defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)

    def helper(node, target, visited):
        stack = [node]
        while stack:
            curNode = stack.pop()
            if curNode not in visited:
                if curNode == target:
                    return True
                visited.add(curNode)
                for nei in graph[curNode]:
                    if nei not in visited:
                        stack.append(nei)
        return False

    visited = set()
    return helper(start, target, visited)

def bfs(start, target):
    q = collections.deque([start])
    visited = set()
    visited.add(start)
    while q:
        curNode = q.popleft()
        if curNode == target:
            return True
        for nei in graph[curNode]:
            if nei not in visited:
                q.append(nei)
                visited.add(nei)
    return False

def dijkstra(start, graph):
    # graph is node: [(neighborNode, weight)]
    n = len(graph)
    shortestPath = {node: float('inf') for node in graph}  # Handles arbitrary node labels
    shortestPath[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        curCost, curNode = heapq.heappop(heap)
        if curNode in visited:
            continue
        visited.add(curNode)
        
        for nei, neiCost in graph[curNode]:
            if nei not in visited:
                newCost = curCost + neiCost
                # Check if new shorter path before traversing node
                if newCost < shortestPath[nei]:
                    shortestPath[nei] = newCost
                    heapq.heappush(heap, (newCost, nei))
    
    return shortestPath

graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start = 0
print(dijkstra(start, graph))  # Output: {0: 0, 1: 3, 2: 1, 3: 4}


class UF:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def isConnected(self, n1, n2):
        return self.find(n1) == self.find(n2)
    
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            if self.rank[p1] > self.rank[p2]:
                self.par[p2] = p1
            elif self.rank[p2] > self.rank[p1]:
                self.par[p1] = p2
            else:
                self.par[p2] = p1
                self.rank[p1] += 1
            return True
        else:
            return False

def kruskals(graph):

    # graph is {node: (neighborNode, cost)}
    heap = []
    for node in graph.keys():
        for nei, neiCost in graph[node]:
            heapq.heappush(heap, (neiCost, node, nei))

    n = len(graph)
    uf = UF(n)

    # Kruskal's Algorithm
    minTreeCost = 0
    mstEdges = 0
    while heap and mstEdges < n -1:
        cost, v1, v2 = heapq.heappop(heap)
        if uf.union(v1, v2):
            minTreeCost += cost
            mstEdges += 1

    return minTreeCost if mstEdges == n-1 else float('inf')

