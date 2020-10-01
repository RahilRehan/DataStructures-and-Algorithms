from tree import *

def identical(node1, node2):
	if node1==None and node2==None:
		return 1
	if node1!=None and node2!=None:
		return node1.val==node2.val and identical(node1.left, node2.left) and identical(node1.right, node2.right) #postorder check
	else:
		return 0

tree = Tree()
tree.insert(16)
tree.insert(9)
tree.insert(25)
tree.insert(3)
tree.insert(13)
tree.insert(18)
tree.insert(30)

tree2 = Tree()
tree2.insert(16)
tree2.insert(9)
tree2.insert(25)
tree2.insert(3)
tree2.insert(13)
tree2.insert(18)
tree2.insert(30)

print("Identical" if identical(tree.root, tree2.root) else "Not Identical")
