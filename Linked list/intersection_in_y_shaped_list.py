"""Given the head of two singly linked lists, return the point where these two linked lists intersect.

Note: It is guaranteed that the intersected node always exists.

Custom Input Format:

head1 contains the nodes before intersection in list1
head2 contains the nodes before intersection in list2
CommonList contains the nodes after intersection of list1 and list2."""

class Solution:
    
    def getIntersectionNode(self, diff, h1, h2):
        curr1 = h1
        curr2 = h2
        for i in range(diff):
            curr1 = curr1.next
                
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            else:
                curr1 = curr1.next
                curr2 = curr2.next
            
    def getCount(self, head):
        cnt = 0
        curr = head
        
        while curr:
            cnt += 1
            curr = curr.next
        return cnt
        
    def intersectPoint(self, head1, head2):
        # code here
        len1 = self.getCount(head1)
        len2 = self.getCount(head2)
        if len1 >= len2:
            diff = len1 - len2
            return self.getIntersectionNode(diff, head1, head2)
        else:
            diff = len2 - len1
            return self.getIntersectionNode(diff, head2, head1)