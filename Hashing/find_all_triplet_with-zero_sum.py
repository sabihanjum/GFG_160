"""Given an array arr[], find all possible triplets i, j, k in the arr[] whose sum of elements is equals to zero. 
Returned triplet should also be internally sorted i.e. i<j<k."""

class Solution:
    def findTriplets(self, arr):
        #set to handle duplicates
        resSet = set()
        n = len(arr)
        mp = {}
        
        #storesum of all pair with their indices
        for i in range(n):
            for j in range(i+1, n):
                s = arr[i] + arr[j]
                
                if s not in mp:
                    mp[s] = []
                    mp[s].append((i, j))
                    
        for i in range(n):
            #find remaining value to get zero sum
            rem = -arr[i]
            if rem in mp:
                for p in mp[rem]:
                    #ensure no 2 indices are same in triplet
                    if p[0] != i and p[1] != i:
                        curr = sorted(i, p[0], p[1])
                        resset.add(tuple(curr))
                        
        return [list(triplet) for triplet in resSet]