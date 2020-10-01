from tree import *

def buildBT(inorder, postorder, start, end):
	global pindex
	if start>end:
		return None
	node = Node(postorder[pindex])
	pindex-=1
	if start==end:
		return node
	iIndex = search(inorder, start, end, node.val) 

	node.right = buildBT(inorder, postorder, iIndex+1, end)
	node.left = buildBT(inorder, postorder, start, iIndex-1)
	return node

def search(arr, start, end, value):
	for i in range(start, end+1):
		if arr[i] == value:
			break
	return i

inorder = [8,4,2,5,1,6,3,7]
postorder = [8,4,5,2,6,7,3,1]
pindex = len(inorder)-1

tree = Tree()
tree.root = buildBT(inorder, postorder, 0, len(inorder)-1)
tree.inorder()

