"""Given an array arr[] and a positive integer k, find the length of the longest subarray with the sum of the elements divisible by k.
Note: If there is no subarray with sum divisible by k, then return 0."""

class Solution:
	def longestSubarrayDivK(self, arr, k):
		#Complete the function
		n = len(arr)
		res = 0
		
		sum = 0
		prefIdx = {}
		
		for i in range(n):
			sum = (sum + arr[i])%k
			if sum == 0:
				res = max(res, i+1)
			elif sum in prefIdx:
				res = max(res, i-prefIdx[sum])
			else:
				prefIdx[sum] = i
		return res