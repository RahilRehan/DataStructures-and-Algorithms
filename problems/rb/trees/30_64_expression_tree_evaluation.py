from tree import *

def evaluate(node):
	if node==None:
		return
	if node.left==None and node.right==None:
		return int(node.val)
	left = evaluate(node.left)
	right = evaluate(node.right)
	print(left, node.val, right)
	if node.val=="+":
		return left+right
	elif node.val=="-":
		return left-right
	elif node.val=="*":
		return left*right
	elif node.val=="/":
		return left/right
	else:
		return -1


tree = Tree()
tree.root = Node("+")
tree.root.left = Node("/")
tree.root.right = Node("-")
tree.root.left.left = Node("*")
tree.root.left.right = Node("5")
tree.root.left.left.left = Node("10")
tree.root.left.left.right = Node("2")
tree.root.right.left = Node("100")
tree.root.right.right = Node("*")
tree.root.right.right.left = Node("3")
tree.root.right.right.right = Node("30")

print(evaluate(tree.root))