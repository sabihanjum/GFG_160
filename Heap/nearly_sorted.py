"""Given an array arr[], where each element is at most k away from its target position, you need to sort the array optimally.
Note: You need to change the given array arr[] in place."""

import heapq
class Solution:

    # Function to sort a nearly sorted array
    # where every element is at most
    # k positions away from its target position.
    def nearlySorted(arr, k):
        # Length of array
        n = len(arr)

        # Creating a min heap
        pq = []

        # Pushing first k elements in pq
        for i in range(k):
            heapq.heappush(pq, arr[i])

        i = k
        index = 0

        while i < n:
            heapq.heappush(pq, arr[i])

            # Size becomes k+1 so pop it
            # and add minimum element in (index) position
            arr[index] = heapq.heappop(pq)
            i += 1
            index += 1

        # Putting remaining elements in array
        while pq:
            arr[index] = heapq.heappop(pq)
            index += 1