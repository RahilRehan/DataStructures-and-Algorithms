def delete_in_middle(node):
    if node is None or node.next is None:
        return
    node.data = node.next.data
    node.next = node.next.next


