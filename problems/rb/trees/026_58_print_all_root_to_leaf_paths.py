#not done yet, there is a mistake

from tree import *

def paths(node, path, l):
	if node==None:
		return
	if node!=None:
		path[l] = node.val
		l+=1
	if node.left==None and node.right==None:
		print(path[:l])
	else:
		paths(node.left, path, l)
		paths(node.right, path, l)

path = [-1]*8

tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(50)
tree.insert(60)

paths(tree.root, path, 0)

	#     90
	#         95
	#   70
	# 65   75
 #  50
	#   60

