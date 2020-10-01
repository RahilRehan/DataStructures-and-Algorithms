# Notes and important points
# Always first check for edge cases in linked lists. Ex: head node
# prev = None and updating it to cur can be useful in many problems
# if working with two linked list, check for empty linked list condition


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def print_list(self):
		cur_node = self.head
		while(cur_node):
			print(cur_node.val, end=", ")
			cur_node = cur_node.next
		print()

	def append(self, val):
		new_node = Node(val)
		#Empty Linked List Case
		if self.head is None:
			self.head = new_node
			return
		#Non Empty Case
		last_node = self.head
		while(last_node.next):
			last_node = last_node.next
		last_node.next = new_node

	def prepend(self, val):
		new_node = Node(val)
		new_node.next = self.head
		self.head =  new_node

	def insert_after_node(self, key, val):
		#we will insert after data
		cur_node = self.head
		while(cur_node):
			if cur_node.val == key:
				break
			cur_node = cur_node.next

		if cur_node is None:
			print("No node found with given value!")
			return 

		new_node = Node(val)
		new_node.next = cur_node.next
		cur_node.next = new_node

	def delete_node(self, key):
		cur_node = self.head
		if cur_node and self.head.val == key:
			self.head = self.head.next
			cur_node = None
			return
		prev = None
		while(cur_node and cur_node.val != key):
			prev = cur_node
			cur_node = cur_node.next
		if cur_node is None:
			return
		prev.next = cur_node.next
		cur_node = None

	def delete_node_at_pos(self, pos):
		cur_node = self.head
		if pos==0 and cur_node:
			self.head = self.head.next
			cur_node = None
			return

		count = 0
		prev = None
		while(count!=pos and cur_node):
			prev = cur_node
			cur_node = cur_node.next
			count+=1
		if cur_node is None:
			return
		prev.next = cur_node.next
		cur_node = None

	def length(self):
		length = 0
		cur_node = self.head
		while(cur_node):
			length+=1
			cur_node = cur_node.next
		return length

	def length_recursive(self, node):
		if node is None:
			return 0
		return 1 + self.length_recursive(node.next)

	def swap_nodes(self, key1, key2):
		if key1==key2:
			return

		cur_node1 = self.head
		prev1 = None
		while(cur_node1 and cur_node1.val!=key1):
			prev1 = cur_node1
			cur_node1 = cur_node1.next

		cur_node2 = self.head
		prev2 = None
		while(cur_node2 and cur_node2.val!=key2):
			prev2 = cur_node2
			cur_node2 = cur_node2.next

		if not cur_node1 or not cur_node2:
			return
		
		if prev1:
			prev1.next = cur_node2
		else:
			self.head = cur_node2

		if prev2:
			prev2.next = cur_node1
		else:
			self.head = cur_node1

		cur_node1.next, cur_node2.next = cur_node2.next, cur_node1.next

	def reverse_iterative(self):
		prev = None
		cur_node = self.head
		while(cur_node):
			nxt = cur_node.next
			cur_node.next = prev
			prev = cur_node
			cur_node = nxt
		self.head = prev

	def reverse_rec(self):
		
		def reverse(cur, prev):
			if not cur:
				return prev
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
			return reverse(cur, prev)

		self.head = reverse(cur = self.head, prev = None)

	def merge_lists(self, llist):
		p = self.head
		q = llist.head
		s = None #smaller node

		#check for empty linked lists
		if not p:
			return q
		if not q:
			return p

		#find head of merged linked list
		if p and q:
			if p.val<= q.val:
				s = p
				p = s.next
			else:
				s = q
				q = s.next
			new_head = s

		#main algorithm, find the smaller node(s) and link respectively

		while(p and q):
			if p.val<=q.val: #p.val is less so point prev small val to new small val
				s.next = p
				s = p
				p = s.next
			else:
				s.next = q
				s = q
				q = s.next

		#handle lists of unequal sizes
		if not p:
			s.next = q
		if not q:
			s.next = p

		return new_head


	def remove_duplicates(self):
		s = set()
		cur = self.head
		prev = None

		while(cur):
			if cur.val in s:
				prev.next = cur.next
				cur = None 
			else:
				s.add(cur.val)
				prev = cur
			cur = prev.next


	def print_kth_from_last(self, k):
		if not self.head:
			return None

		p = self.head
		q = self.head

		count = 0
		while q:
			count+=1
			if count>=k:
				break
			q = q.next
		
		while p and q.next:
			p = p.next
			q = q.next

		return p.val

	def count_occurences_recursive(self, key):

		def count_occurences(node, key):
			if not node:
				return 0
			if node.val == key:
				return 1 + count_occurences(node.next, key)
			else:
				return count_occurences(node.next, key)

		return count_occurences(self.head, key)

	def rotate(self, k):
	  if self.head and self.head.next:
	  	count = 0
	  	p, q = self.head, self.head

	  	prev = None
	  	while p and count<k:
	  		prev = p
	  		p = p.next
	  		q = q.next
	  		count += 1

	  	p = prev

	  	while q:
	  		prev = q
	  		q = q.next
	  	q = prev

	  	q.next = self.head
	  	self.head = p.next
	  	p.next = None 

	def is_palindrome(self):
		p = self.head
		s = ""
		while p:
			s+=p.val
			p = p.next
		return s==s[::-1]

	def move_tail_to_head(self):
		p = self.head
		prev = None
		while p and p.next:
			prev = p
			p = p.next
		prev.next = None
		p.next = self.head
		self.head = p

			


ll = LinkedList()

ll.append(2)
ll.append(3)
ll.append(5)
ll.delete_node(5)
ll.print_list()

# ll.append(6)
# ll.prepend(1)
# ll.insert_after_node(3, 4)
# ll.insert_after_node(6, 7)
# ll.print_list()
# ll.delete_node(4)
# ll.print_list()
# print("Lenght is, ", ll.length_recursive(ll.head))
# ll.swap_nodes(1, 7)
# ll.print_list()
# ll.reverse_rec()
# ll.print_list()


#merge lists test
# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_lists(llist_2)
# llist_1.print_list()

#remove duplicates test
# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

#kth node from last test
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# print(llist.print_kth_from_last(4))
# print(llist.print_kth_from_last(3))


#recursive count elements
# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_recursive(1))

#rotate test
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)

# llist.rotate(4)
# llist.print_list()

#ispalindrome test, approaches: string, stack and two pointer with array
# llist_2 = LinkedList()
# llist_2.append("A")
# llist_2.append("B")
# llist_2.append("A")
# print(llist_2.is_palindrome())

#move tail to head test
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)
# llist.move_tail_to_head()
# llist.print_list()