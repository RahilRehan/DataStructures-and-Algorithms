from ll import *


def kth_to_last(node, k):
    runner = node
    for _ in range(k):
        if runner is None:
            return None
        runner = runner.next

    while(runner is not None):
        runner = runner.next
        node = node.next
    return node


#yet to solve it recursively


ll = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.insert(7)
ll.insert(8)



ll.print_list()
print("*****Kth to Last*****")
print(kth_to_last(ll.head,4))
