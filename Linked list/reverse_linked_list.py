"""Given the head of a linked list, the task is to reverse this list and return the reversed head."""

class Solution:
    def reverseList(self, head):
        # Code here
        curr = head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next
        head = prev
        return head
