class DFS():
	def __init__(self, n):
		self.graph = {0:[1], 1:[0, 2], 2: [1, 3], 3: [2], 4: [5, 7], 5: [4, 6, 7], 6: [5, 7], 7:[4, 5, 6]}
		self.visited = [False]*n
		self.components = 0

	def dfs_util(self, node):
		if self.visited[node]:
			return
		self.visited[node] = True
		print(node)
		self.visited[node] = True
		for nei in self.graph[node]:
			self.dfs_util(nei)

	def dfs(self, source): # dfs from a given source node
		self.dfs_util(source)

	def dfs_components(self): # dfs to all nodes and find number of connected components
		for node in self.graph:
			if self.visited[node]==False:
				self.components+=1
				self.dfs_util(node)
		print("Number of connected components are; ", self.components)


# Time complexity is O(V+E)
# space is O(N) for stack
# https://www.quora.com/Why-is-the-complexity-of-DFS-O-V+E

d = DFS(8)
d.dfs(2)
d.dfs_components()

