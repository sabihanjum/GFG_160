"""Given an array arr[] of positive integers. Find the number of pairs of integers whose absolute difference equals to a given number k.
Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

The answer is guaranteed to fit in a 32-bit integer."""

class Solution:
    def countPairs(self, arr, k):
        # code here
        freq = {}
        cnt = 0

        for i in range(len(arr)):
            if arr[i] + k in freq:
                cnt += freq[arr[i] + k]

            if arr[i] - k in freq:
                cnt += freq[arr[i] - k]

            freq[arr[i]] = freq.get(arr[i], 0) + 1

        return cnt
