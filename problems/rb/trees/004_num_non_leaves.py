from tree import *

#Number of Non leave nodes

def non_leaves(node):
	if node==None:
		return 0
	if not node.left and not node.right:
		return 0
	return 1 + non_leaves(node.left) + non_leaves(node.right)

tree = Tree()
populate(tree)
print(non_leaves(tree.root))
