**Linked List Problems**

1. [Kth node from end of linked list:](https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/842759/Python-JavaScript-C%2B%2B-clean-solution.)
    * hash based approach
    * slow/fast pointers
  
2. [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/discuss/842874/Python-JavaScript-C%2B%2B-clean-solutions.)
    * hash based
    * slow/fast pointers

3. [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/discuss/843844/Python-JavaScript-C%2B%2B-clean-solutions.)
    * append to string and check for palindrone
    * slow/fast , split in middle and check both halves

4. [Intersection of two linked lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
    * find length of two linked lists, find difference between them, substract and traverse

5. [Clone double linked list with one random pointer](https://leetcode.com/problems/copy-list-with-random-pointer/discuss/853210/Python-two-clean-solutions.)

6. [XOR linked list](https://www.geeksforgeeks.org/xor-linked-list-a-memory-efficient-doubly-linked-list-set-1/)
    * assumptions: 
      * addresses have same number of bits 
      * insert at beginning link(node)= push(null, head)
    * let linked list be "None, A, B, C, D, E, None"
    * example: link(A) = None ^ addr(B)
    * link(C) = addr(B) ^ addr(D)
    * forward traversal - xor(prev, link(cur))
    * backward traversal - xor(next, link(cur))

7. [Split circular linked list]
    * fast and slow pointers

8. [Reverse k nodes in linked list](https://leetcode.com/problems/reverse-nodes-in-k-group/)
    * use recursion, check my own leetcode submission
    * similar problem : reverse k alternate nodes in linked list
    * ex: 1->2->3->4->5->6->7, k = 2  2->1->3->4->6->5->7
    * second problem approach: reverse(k), traverse(k) and recur 
    * don't forget about space complexity due to recursion o(n/k)
    * [link](https://www.hackerrank.com/contests/applied-course/challenges/reverse-alternative-k-nodes/submissions/code/1326671326)

9. [Add numbers](https://leetcode.com/problems/add-two-numbers/)
    * take care about carry
  
10. [Merge Two sorted linked lists](https://leetcode.com/problems/merge-two-sorted-lists/submissions/)
    * Space efficient version without a new linked list, (latest submission on leetcode)

11. [Merge k-sorted linked lists](https://leetcode.com/problems/merge-k-sorted-lists)
