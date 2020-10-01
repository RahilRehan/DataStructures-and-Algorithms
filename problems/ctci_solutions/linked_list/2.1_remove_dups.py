from ll import *

def remove_dup_1(node):
    s = set()
    prev = None
    while(node is not None):
        if(node.val in s):
            prev.next = node.next
        else:
            s.add(node.val)
            prev = node
        node = node.next

#5,3,4,3,4,1,5,1   => 5,3,4,1

#iterative without extra space takes time complexity of O(N^2)
def remove_dup_follow_up(head):
    node = head
    while(node):
        runner = node
        while(runner.next):
            if(runner.next.val == node.val):
                node.next = runner.next.next
            else:
                runnner = runner.next
        node = node.next
    return head





ll = LinkedList()

ll.insert(1)
ll.insert(5)
ll.insert(1)
ll.insert(4)
ll.insert(3)
ll.insert(4)
ll.insert(3)
ll.insert(5)

ll.print_list()
print("*****removed dups******")
remove_dup_follow_up(ll.head)
ll.print_list()



