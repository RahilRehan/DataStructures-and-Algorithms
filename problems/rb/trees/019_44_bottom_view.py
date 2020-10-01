from tree import *

k = dict()

def vertical_order(node, hd):
	if not node:
		return
	k[hd] = node.val
	vertical_order(node.left, hd-1)
	vertical_order(node.right, hd+1)

tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(50)
tree.insert(60)

vertical_order(tree.root, 0)

mi = min(k.keys())
ma = max(k.keys())

for i in range(mi, ma+1):
	print('Nodes present at {0} are {1}'.format(i, k[i]))

