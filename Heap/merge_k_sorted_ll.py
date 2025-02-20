"""Given an array arr[] of n sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list, then return the head of the merged linked list."""

import heapq
        
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        pq = []
        for i in range(len(arr)):
            head = arr[i]
            if head:
                heapq.heappush(pq, (head.data, head))
        dummy = Node(-1)
        curr = dummy
        
        while pq:
            data, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(pq, (node.next.data, node.next))
                
        return dummy.next