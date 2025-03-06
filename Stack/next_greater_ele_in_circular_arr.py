"""Given a circular integer array arr[], the task is to determine the next greater element (NGE) for each element in the array.

The next greater element of an element arr[i] is the first element that is greater than arr[i] when traversing circularly. If no such element exists, return -1 for that position.

Circular Property:

Since the array is circular, after reaching the last element, the search continues from the beginning until we have looked at all elements once"""

class Solution:
    def nextLargerElement(arr):
        n = len(arr)

        # to store the results
        res = [-1] * n

        # Iterate for all the elements of the array
        for i in range(n):

            for j in range(1, n):

                # Checking for next greater element
                if arr[i] < arr[(i + j) % n]:

                    res[i] = arr[(i + j) % n]
                    break

        return res