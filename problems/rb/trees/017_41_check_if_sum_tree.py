# Sum Tree => At each node sum of nodes below it must sum to the current node.

from tree import *

def is_sum_tree(node):
	if not node:
		return 0
	if not node.left and not node.right:
		return node.val

	l = is_sum_tree(node.left)
	r = is_sum_tree(node.right)

	if l==-1 or r==-1:
		return -1

	if (l+r == node.val):
		return 2*node.val

	return -1

tree = Tree()
tree.root = Node(50)
tree.root.left = Node(15)
tree.root.left.left = Node(10)
tree.root.left.right = Node(5)
tree.root.right = Node(10)
tree.root.right.left = Node(7)
tree.root.right.right = Node(3)

print("Is a sum tree" if is_sum_tree(tree.root)>-1 else "Not a sum tree")





