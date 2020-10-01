from tree import *

#given a sorted array form a balanced BST

#approach 1: take each node and do avl => as max height of tree is lg(n)  => t.c would be O(nlogn).

#approach 2: find middle, make root node and recursively build tree.


# 5 10 20 30 40 50 55


#           30
#   5 10 20    40 50 55
  

#   	   30
#     10         50
#  5     20   40    55

def build_bst(node, arr, l, r):
	if l>r:
		return None		
	mid = (l+r)//2
	node = Node(arr[mid])
	node.left = build_bst(node, arr, l, mid-1)
	node.right = build_bst(node, arr, mid+1, r)
	return node

arr = [5,10,20,30,40,50,55]

tree = Tree()
tree.root = build_bst(tree.root, arr, 0, len(arr)-1)
tree.inorder()

