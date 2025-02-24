"""Given an array arr[ ] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1."""

class Solution:
    def nextLargerElement(arr):
        n = len(arr)
        res = [-1] * n  
        stk = []  

        # Traverse the array from right to left
        for i in range(n - 1, -1, -1):

            # Pop elements from the stack that are less 
            # than or equal to the current element
            while stk and arr[stk[-1]] <= arr[i]:
                stk.pop()

            # If the stack is not empty, the element at the 
            # top of the stack is the next greater element
            if stk:
                res[i] = arr[stk[-1]]

            # Push the current index onto the stack
            stk.append(i)

        return res