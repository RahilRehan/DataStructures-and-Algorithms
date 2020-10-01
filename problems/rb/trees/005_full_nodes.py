from tree import *

#nodes count with both the children

def full_nodes(node):
	if node==None:
		return 0
	if not node.left and not node.right:
		return 0

	return full_nodes(node.left) + \
		   full_nodes(node.right) + \
		   (1 if (node.left is not None and node.right is not None) else 0)

tree = Tree()
populate(tree, 10, 100)  #tree, num_nodes, max_int
print(full_nodes(tree.root))
