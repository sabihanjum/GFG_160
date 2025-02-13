"""Given a head singly linked list of positive integers. The task is to check if the given linked list is palindrome or not."""

class Solution:
    def reverse(self, head):
        curr = head
        prev = None
        
        while curr:
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next
        return prev
    def CompareList(self, head, head2):
        curr = head
        curr2 = head2
        
        while curr and curr2:
            if curr.data != curr2.data:
                return False
            curr = curr.next
            curr2 = curr2.next
        return True
            
    def isPalindrome(self, head):
        #code here
        if head is None or head.next is None:
            return True
            
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        head2 = self.reverse(slow.next)
        slow.next = None
        
        ret = self.CompareList(head, head2)
        head2 = self.reverse(head2)
        
        slow.next = head2
        
        return ret