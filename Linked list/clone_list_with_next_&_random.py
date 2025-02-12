"""You are given a special linked list with n nodes where each node has two pointers a next pointer that points to the next node of the singly linked list, and a random pointer that points to the random node of the linked list.

Construct a copy of this linked list. The copy should consist of the same number of new nodes, where each new node has the value corresponding to its original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list, such that it also represent the same list state. None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

NOTE : Original linked list should remain unchanged."""

class Solution:
    def cloneLinkedList(self, head):
        # code here
        curr = head
        while curr:
            newNode = Node(curr.data)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
        curr = head
        
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        cloneHead = head.next
        curr = head
        cloneCurr = cloneHead
        
        while cloneCurr.next:
            curr.next = curr.next.next
            cloneCurr.next = cloneCurr.next.next
            
            curr = curr.next
            cloneCurr = cloneCurr.next
            
        curr.next = None
        cloneCurr.next = None
        
        return cloneHead
