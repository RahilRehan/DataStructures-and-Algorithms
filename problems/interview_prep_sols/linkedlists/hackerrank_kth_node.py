class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LL:
    def __init__(self):
        self.head = None

    def initialize(self, arr):
        for ele in arr:
            self.insert(ele)

    def insert(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next


n, k = list(map(int, input().split()))
li = list(map(int, input().split()))
ll = LL()
ll.initialize(li)
ll.print()
