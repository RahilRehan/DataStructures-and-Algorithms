from tree import *

k = dict()

def vertical_order_sum(node, hd):
	if not node:
		return
	if hd in k.keys():
		k[hd].append(node.val)
	else:
		k[hd] = [node.val]
	vertical_order_sum(node.left, hd-1)
	vertical_order_sum(node.right, hd+1)

tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(50)
tree.insert(60)

vertical_order_sum(tree.root, 0)

mi = min(k.keys())
ma = max(k.keys())

for i in range(mi, ma+1):
	print('Nodes present at {0} are {1}'.format(i, 	k[i]))

for i in range(mi, ma+1):
	print('Sum of nodes present at {0} are {1}'.format(i, sum(k[i])))

