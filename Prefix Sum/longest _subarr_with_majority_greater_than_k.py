"""Given an array arr[] and an integer k, the task is to find the length of longest subarray in which the count of elements greater than k is more than the count of elements less than or equal to k."""

class Solution:
    def longestSubarray(arr, k):
        n = len(arr)
        prefIdx = {}
        sum = 0
        res = 0

        # Traverse through all subarrays
        for i in range(n):
            # Consider arr[i] <= k as -1 and arr[i] > k as +1
            sum += 1 if arr[i] > k else -1

            # make an entry for sum if it is not present
            # in the hash map
            if sum not in prefIdx:
                prefIdx[sum] = i

            # If all elements are smaller than k, return 0
        if -n in prefIdx:
            return 0
        prefIdx[-n] = n

        # For each sum i, update prefIdx[i] with 
        # min(prefIdx[-n], prefIdx[-n+1] .... pref[i])
        for i in range(-n + 1, n + 1):
            if i not in prefIdx:
                prefIdx[i] = prefIdx[i - 1]
            else:
                prefIdx[i] = min(prefIdx[i], prefIdx[i - 1])

        # To find the longest subarray with sum > 0 ending at i,
        # we need left-most occurrence of s' such that s' < s.
        sum = 0
        for i in range(n):
            sum += 1 if arr[i] > k else -1
            if sum > 0:
                res = i + 1
            else:
                res = max(res, i - prefIdx[sum - 1])

        return res