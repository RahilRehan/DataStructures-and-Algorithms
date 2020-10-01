# this is binary tree, therefore properties of search wont work like in the last problem
from tree import *

def common_ans_bt(node, p, q):
	if node==None:
		return
	if node.val==p or node.val==q:
		return node
	else:
		l = common_ans_bt(node.left, p, q)
		r = common_ans_bt(node.right, p, q)
		if l!=None and r!=None:
			return node
		return l if l!=None else r

tree = Tree()
tree.insert(16)
tree.insert(9)
tree.insert(25)
tree.insert(3)
tree.insert(13)
tree.insert(18)
tree.insert(30)

print(common_ans_bt(tree.root, 25, 18).val)

