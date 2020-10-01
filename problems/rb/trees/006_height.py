from tree import *

def height(node):
	if node==None:
		return 0
	if not node.left and not node.right:  #if leaf, depends on definition of height 1 or 0
		return 0
	return 1 + max( height(node.left) , height(node.right) ) 

tree = Tree()
populate(tree)
print(height(tree.root))