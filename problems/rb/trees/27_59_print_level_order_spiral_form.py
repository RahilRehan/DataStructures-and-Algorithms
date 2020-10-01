from tree import *

s1 = []
s2 = []

def level_spiral(node):
	s1.append(node)
	while(len(s1)>0 or len(s2)>0):
		while len(s1)>0:
			temp = s1.pop()
			print(temp.val)
			if temp.right:
				s2.append(temp.right)
			if temp.left:
				s2.append(temp.left)
		while len(s2)>0:
			temp = s2.pop()
			print(temp.val)
			if temp.left:
				s1.append(temp.left)
			if temp.right:
				s1.append(temp.right)



tree = Tree()
tree.insert(90)
tree.insert(95)
tree.insert(70)
tree.insert(65)
tree.insert(70)
tree.insert(75)
tree.insert(50)
tree.insert(60)

level_spiral(tree.root)