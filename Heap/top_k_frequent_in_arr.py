"""Given a non-empty integer array arr[] of size n, find the top k elements which have the highest frequency in the array.

Note: If two numbers have the same frequencies, then the larger number should be given more preference."""
import heapq
from collections import Counter
class Solution:
    # Function to find k numbers with most occurrences
    def topKFrequent(arr, k):

        # Dictionary 'mp' implemented as frequency hash
        # table
        mp = Counter(arr)

        pq = []
    
        for key, value in mp.items():
            heapq.heappush(pq, (value, key))
            if len(pq) > k:
                heapq.heappop(pq)

        # store the result
        res = []
    
        while pq:
            res.append(heapq.heappop(pq)[1])

        res.reverse()
        return res