

# Linked list vs array diff
# linked list can insert elements more efficiently, esp at the ends
# linked list read at O(N), insert and delete at O(1)
# Array read at O(1), but linked list read at O(N)
# Use linked list when there are more writes than reads

# Singly Linked List: Each node has a pointer to the next node only, allowing for traversal in one direction, from head to tail.
# A Singly LinkedList only need to store a head and tail of listnode.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head

    def insert_end(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def print(self):
        curr = self.head.next
        values = []
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(values))


ll = LinkedList()
ll.insert_end(2)
ll.insert_end(5)
ll.insert_end(12)
ll.print()
