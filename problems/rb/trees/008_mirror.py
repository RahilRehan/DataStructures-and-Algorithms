from tree import *

def mirror(node):
	if node==None:
		return
	mirror(node.right)
	mirror(node.left)
	node.left, node.right = node.right, node.left



tree = Tree()
tree.insert(16)
tree.insert(9)
tree.insert(25)
tree.insert(3)
tree.insert(13)
tree.insert(18)
tree.insert(30)

print("Inorder is: ")
tree.inorder()
mirror(tree.root)
print("Inorder after mirror: ")
tree.inorder()
