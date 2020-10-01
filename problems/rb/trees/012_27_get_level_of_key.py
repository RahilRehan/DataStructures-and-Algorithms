from tree import *

def get_level(node, level, key):
	if node==None:
		return -1
	if node.val==key:
		return level
	level2 = get_level(node.left, level+1, key)

	if level2!=-1:
		return level2
	return get_level(node.right, level+1, key)

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

print(get_level(tree.root, 1, 30))