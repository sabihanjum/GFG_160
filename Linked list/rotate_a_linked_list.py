"""Given the head of a singly linked list, your task is to left rotate the linked list k times."""

class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        # code here
        if k == 0 or head is None:
            return head
            
        len = 1
        curr = head
        
        while curr.next is not None:
            len += 1
            curr = curr.next
            
        k = k%len
        
        if k == 0:
            return head
        curr.next = head
        
        curr = head
        
        for i in range(1, k):
            curr = curr.next
            
        head = curr.next
        curr.next = None
        
        return head