from tree import *

def diameter(node):
	if node==None:
		return 0
	l = diameter(node.left)
	r = diameter(node.right)
	return max(l, r) + 1
	

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


print(diameter(tree.root))
