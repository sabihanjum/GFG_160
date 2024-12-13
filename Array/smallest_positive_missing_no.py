"""You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.

Note: Positive number starts from 1. The array can have negative integers too."""

class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Rearrange the array such that arr[i] = i + 1 if possible
        for i in range(n):
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                # Swap arr[i] and arr[arr[i] - 1] to place arr[i] at its correct position
                temp = arr[i]
                arr[i] = arr[temp - 1]
                arr[temp - 1] = temp

        # Check for the first missing positive number
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # If all numbers from 1 to n are present, the missing number is n + 1
        return n + 1
