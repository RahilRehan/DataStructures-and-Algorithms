from tree import *

def common_ans_bst(node, p, q):
	if node==None:
		return
	if node.val==p or node.val==q:
		return node
	if p < node.val and q > node.val:
		return node
	else:
		l = common_ans_bst(node.left, p, q)
		r = common_ans_bst(node.right, p, q)
		return l if l!=None else r


tree = Tree()
tree.insert(16)
tree.insert(9)
tree.insert(25)
tree.insert(3)
tree.insert(13)
tree.insert(18)
tree.insert(30)

print(common_ans_bst(tree.root, 3, 13).val)
