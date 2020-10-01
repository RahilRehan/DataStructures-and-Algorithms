#approach: create a new empty tree and start building avl tree, o(nlogn)
#approach: find inorder arr, build bal_bst from sorted arr like in prvs prob

from tree import *
s_arr = []

def inorder(node):
	if node==None:
		return 
	inorder(node.left)
	s_arr.append(node.val)
	inorder(node.right)


def build_bst(node, arr, l, r):
	if l>r:
		return None		
	mid = (l+r)//2
	node = Node(arr[mid])
	node.left = build_bst(node, arr, l, mid-1)
	node.right = build_bst(node, arr, mid+1, r)
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

inorder(tree.root)
tree.root = build_bst(tree.root, s_arr, 0, len(s_arr)-1)
tree.inorder()