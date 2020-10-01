from tree import *

def postorder(node):
	if node:
		postorder(node.left)
		postorder(node.right)
		print(node.val)

def preorder(node):
	if node:
		print(node.val)
		preorder(node.left)
		preorder(node.right)

tree = Tree()
populate(tree)

print("Inorder:")
tree.inorder()
print("Postorder:")
postorder(tree.root)
print("Preorder:")
preorder(tree.root)