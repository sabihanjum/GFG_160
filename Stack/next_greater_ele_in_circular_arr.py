"""Given a circular integer array arr[], the task is to determine the next greater element (NGE) for each element in the array.

The next greater element of an element arr[i] is the first element that is greater than arr[i] when traversing circularly. If no such element exists, return -1 for that position.

Circular Property:

Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once"""

class Solution:
    def nextLargerElement(arr):
        n = len(arr)
        res = [-1] * n
        stk = []
    
        # Traverse the array from right to left
        for i in range(2 * n - 1, -1, -1):
    
            # Pop elements from the stack that are less
            # than or equal to the current element
            while stk and stk[-1] <= arr[i % n]:
                stk.pop()
            
            # If the stack is not empty, the top element
            # is the next greater element
            if i < n and stk:
                res[i] = stk[-1]
            
            # Push the current element onto the stack
            stk.append(arr[i % n])
        
        return res