from tree import *

def num_leaves(node):
	if node==None:
		return 0
	elif not node.left and not node.right:
		return 1
	else:
		return num_leaves(node.left) + num_leaves(node.right)

tree = Tree()
populate(tree, 12, 100)

print(num_leaves(tree.root))
