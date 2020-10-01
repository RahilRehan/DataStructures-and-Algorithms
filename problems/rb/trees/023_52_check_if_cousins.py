from tree import *

def level(node, a, l):
	if node==None:
		return -1
	if node.val==a:
		return l
	left = level(node.left, a, l+1)
	if left!=-1:
		return left
	return level(node.right, a, l+1)

def same_parent(node, a, b):
	if node==None:
		return 0
	return (node.left and node.left.val==a) and (node.right and node.right.val==b) or \
			(node.left and node.left.val==b) and (node.right and node.right.val==a) or \
			same_parent(node.left, a, b) or \
			same_parent(node.right, a, b)


def is_cousin(node, a, b):
	if (level(node, a, 1)==level(node, b, 1) and (not same_parent(node, a, b))):
		return 1
	else:
		return 0
	

tree = Tree()
tree.insert(50)
tree.insert(40)
tree.insert(60)
tree.insert(30)
tree.insert(45)
tree.insert(55)
tree.insert(70)

print(is_cousin(tree.root, 45, 30))
print(is_cousin(tree.root, 45, 55))
print(is_cousin(tree.root, 40, 45))

 #       50
 # 		/   \
 #    40     60
 #    / \   /  \
 #  30  45 55  70

 # 30 and 55 are cousins as they are on same level but different parents.
