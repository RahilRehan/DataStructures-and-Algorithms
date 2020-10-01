# 94.Leetcode, Binary Tree Inorder Traversal

from tree import *

def inorder_iterative(root):
    stack = []
    traversal = []

    while(root or stack):
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            traversal.append(root.val)
            root = root.right
    return traversal


tree = Tree()
populate(tree, 12, 100)  #tree, num_nodes, max_int
print(inorder_iterative(tree.root))