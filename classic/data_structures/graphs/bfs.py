from collections import deque
class BFS():
	def __init__(self, n):
		self.graph = {0:[1], 1:[0, 2], 2: [1, 3], 3: [2, 4, 5], 4: [3, 5, 7], 5: [3, 4, 6, 7], 6: [5, 7], 7:[4, 5, 6]}
		self.dist = [0]*n # noting distances
		self.pred = [-1]*n  # predecesor list to store predecesors of nodes
		self.visited = [False]*n

	def bfs(self, source):   #standard implementation
		queue = [source]
		self.visited[source] = True

		while queue:
			current = queue.pop(0)
			print(current)
			for i in range(len(self.graph[current])):
				if self.visited[self.graph[current][i]] == False:
					queue.append(self.graph[current][i])
					self.dist[self.graph[current][i]] = self.dist[current]+1
					self.pred[self.graph[current][i]]
					self.visited[self.graph[current][i]] = True

	def bfs_template(self, source):  #implementation for problem solving
		q = deque([source])
		self.visited[source] = True
		while q:
			cur = q.popleft()
			print(cur)  #do stuff
			for nei in self.graph[cur]:
				if self.visited[nei] == False:
					q.append(nei)
					self.visited[nei] = True

#Time complexity -> in worst we could have n adjacent vertices for n vertices \
#					=> then number of edges are n*(n-1)/2. i.e O(V^2) but usually O(V+E)

# https://www.quora.com/What-is-the-time-complexity-of-Breadth-First-Search-Traversal-of-a-graph

#Auxilary Space complexity -> O(N) for queue and visited

b = BFS(8)
b.bfs_template(2)
