# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        h1 = head

        # Pass 1: clone and interweave
        while h1:
            h2 = Node(h1.val) # clone(h1)
            h2.next = h1.next
            h1.next = h2
            h1 = h2.next

        # Pass 2: set random pointers
        h1 = head
        while h1:
            h2 = h1.next
            if h1.random:
                h2.random = h1.random.next # h2.random = h1.random.next
            else:
                h2.random = None
            h1 = h2.next

        # Pass 3: separate the lists
        h1 = head
        h2 = head.next
        new_head = h2

        while h1 and h2:
            h1.next = h2.next # h1.next = h2.next
            h1 = h1.next

            if h1:
                h2.next = h1.next # h2.next = h1.next
                h2 = h2.next

        return new_head