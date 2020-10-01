from tree import *

def level_order(node):
	que = []
	que.append(node)
	while(len(que)>0):
		ele = que[0]
		print(ele.val)
		que = que[1:]
		if ele.left:
			que.append(ele.left)
		if ele.right:
			que.append(ele.right)


tree = Tree()
tree.insert("a")
tree.insert("b")
tree.insert("c")
tree.insert("d")
tree.insert(13)
tree.insert(18)
tree.insert(30)
print("Inorder is: ")
tree.inorder()
print("Level Order is: ")
level_order(tree.root)