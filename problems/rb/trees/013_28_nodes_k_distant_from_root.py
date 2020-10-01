from tree import *

def node_k_dist(node, k, dist):
	if node==None:
		return
	if(k==dist):
		print(node.val)
	node_k_dist(node.left, k, dist+1)
	node_k_dist(node.right, k, dist+1)

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

print(node_k_dist(tree.root, 3, 1))