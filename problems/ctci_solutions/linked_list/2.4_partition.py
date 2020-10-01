from ll import *

def partition(node, x):
    head = node
    tail = node
    while(node is not None):
        nxt = node.next
        if(node.val < x):
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = nxt
    tail.next = None
    return head



ll = LinkedList()
ll.insert(2)
ll.insert(10)
ll.insert(1)
ll.insert(5)
ll.insert(6)
ll.insert(3)
ll.insert(8)

ll.print_list()
print("****After Parition****")
ll.head = partition(ll.head, 5)
ll.print_list()
