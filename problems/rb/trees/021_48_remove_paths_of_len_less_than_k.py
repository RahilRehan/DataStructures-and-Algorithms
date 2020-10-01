from tree import *
# Remove all the paths from the tree whose length is less than k
# postorder traversal

def remove_path(node, k):
	if node==None:
		return None
	if k==0:
		return node
	node.left = remove_path(node.left, k-1)
	node.right = remove_path(node.right, k-1)

	if node.left==None and node.right==None:
		del node
		return None
	return node


tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(50)
tree.insert(60)


remove_path(tree.root, k=4)
tree.inorder()