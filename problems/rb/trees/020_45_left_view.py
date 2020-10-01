from tree import *

maxi = 0

def left_view(node, level):
	global maxi
	if node:
		if maxi < level:
			print(node.val)
			maxi = level
		left_view(node.left, level+1)
		left_view(node.right, level+1)


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

left_view(tree.root, 1)