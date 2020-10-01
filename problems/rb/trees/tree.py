class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, val):
		if self.root==None:
			self.root = Node(val)
		else:
			self._insert(self.root, val)

	def _insert(self, curr, val):
		if curr.val > val:
			if curr.left==None:
				curr.left = Node(val)
			else:
				self._insert(curr.left, val)
		else:
			if curr.right==None:
				curr.right = Node(val)
			else:
				self._insert(curr.right, val)

	def inorder(self):
		if self.root!=None:
			self._inorder(self.root)

	def _inorder(self, node):
		if node:
			self._inorder(node.left)
			print(node.val)
			self._inorder(node.right)

def populate(tree, num_ele=10, max_int = 100):
	from random import randint
	for _ in range(num_ele):
		cur_ele = randint(0, max_int)
		tree.insert(cur_ele)
	return tree

