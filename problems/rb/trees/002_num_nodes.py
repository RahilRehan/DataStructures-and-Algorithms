from tree import *

def num_nodes(node):
	if node==None:
		return 0
	else:
		return 1 + (num_nodes(node.left) + num_nodes(node.right))

tree = Tree()
populate(tree, 12, 100)  #tree, num_nodes, max_int
print(num_nodes(tree.root))
