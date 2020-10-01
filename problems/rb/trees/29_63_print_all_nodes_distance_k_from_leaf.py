from tree import *

def nodes_k_leaf(node, k, cur_i):
	global path,ansrs
	if node==None:
		return
	path.append(node)
	if node.left==None and node.right==None:
		if cur_i-k>=0:
			ansrs.add(path[-(k+1)])
			path.pop()
		return
	nodes_k_leaf(node.left, k, cur_i+1)
	nodes_k_leaf(node.right, k, cur_i+1)
	path.pop()

path = []
ansrs = set()

tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(93)
tree.insert(100)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(50)
tree.insert(60)

nodes_k_leaf(tree.root, 2, 0)

for node in ansrs:
	print(node.val, end=" ")

