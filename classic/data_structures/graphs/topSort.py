class TopSort:
    def __init__(self, n):
        self.graph = {0:[], 1:[], 2:[3], 3:[1], 4:[0, 1], 5:[2, 0]}
        self.visited = [False]*n
        self.topsorted = []

    def dfs(self, node):
        self.visited[node] = True
        for nei in self.graph[node]:
            if self.visited[nei]==False:
                self.dfs(nei)   
        self.topsorted.insert(0, node)


    def topologicalSort(self, n):
        for node in range(n):
            if self.visited[node] == False:
                self.dfs(node)
        return self.topsorted


ts = TopSort(6)
print(ts.topologicalSort(6))
