"""Given the head a linked list, the task is to reverse every k node in the linked list. If the number of nodes is not a multiple of k then the left-out nodes in the end, should be considered as a group and must be reversed."""

class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        curr = head
        newHead = None
        tail = None
        
        while curr:
            groupHead = curr
            count = 0
            prev = None
            
            while curr and count<k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            if newHead is None:
                newHead = prev
                
            if tail is not None:
                tail.next = prev
                
            tail = groupHead
        return newHead