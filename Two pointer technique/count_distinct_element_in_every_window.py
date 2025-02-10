"""Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array."""

class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n = len(arr)
        res = []
        freq = defaultdict(int)
        
        for i in range(k):
            freq[arr[i]] += 1
        res.append(len(freq))
        
        for i in range(k, n):
            freq[arr[i]] += 1
            freq[arr[i-k]] -= 1
            
            if freq[arr[i-k]] == 0:
                del freq[arr[i-k]]
            res.append(len(freq))
    
        return res