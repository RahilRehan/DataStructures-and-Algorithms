class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn

    def print_list(self):
        temp = self.head
        while(temp is not None):
            print(temp.val)
            temp = temp.next
