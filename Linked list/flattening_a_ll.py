"""Given a linked list containing n head nodes where every node in the linked list contains two pointers:
(i) next points to the next node in the list.
(ii) bottom pointer to a sub-linked list where the current node is the head.
Each of the sub-linked lists nodes and the head nodes are sorted in ascending order based on their data.
Your task is to flatten the linked list such that all the nodes appear in a single level while maintaining the sorted order.

Note:
1. ↓ represents the bottom pointer and -> represents the next pointer.
2. The flattened list will be printed using the bottom pointer instead of the next pointer."""

from heapq import heappush, heappop

class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.bottom = None

# Utility function to insert a node at beginning
# of the linked list
def push(head, data):
    newNode = Node(data)
    newNode.bottom = head
    head = newNode
    return head

def printList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.bottom
    print()

# Class to compare two node objects
class Cmp:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.data < other.node.data

class Solution:
    def flatten(self, root):
        pq = []
        head = None
        tail = None

        # Pushing main link nodes into priority_queue
        while root:
            heappush(pq, Cmp(root))
            root = root.next

        # Extracting the minimum node while the priority 
        # queue is not empty
        while pq:
            minNode = heappop(pq).node

            if head is None:
                head = minNode
                tail = minNode
            else:
                tail.bottom = minNode
                tail = tail.bottom

            # If we have another node at the bottom of the popped 
            # node, push that node into the priority queue
            if minNode.bottom:
                heappush(pq, Cmp(minNode.bottom))

            # Detach the node from its next link
            minNode.next = None

        return head
