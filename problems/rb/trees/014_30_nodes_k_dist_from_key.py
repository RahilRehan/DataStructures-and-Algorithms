from tree import *
from collections import deque

def distanceK(root, target, K):
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = deque([(target, 0)])
        seen = {target}  #set
        an = []
        while queue:
            if queue[0][1] == K:
                return [node.val for node,d in queue]
            node, d = queue.popleft()
            for nn in (node.left, node.right, node.par):
                if nn and nn not in seen:
                    seen.add(nn)
                    queue.append((nn, d+1))
        return []

tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(80)
tree.insert(85)
tree.insert(50)
tree.insert(60)
tree.insert(40)
tree.insert(30)

print(distanceK(tree.root, tree.root.left, 2))