"""Given an array arr[] and a target, your task is to find all unique combinations in the array where the sum is equal to target. Each number in arr[] may only be used once in the combination.

You can return your answer in any order."""

class Solution:
    def findCombinations(self, arr, index, target, curr, res):
        # If a unique combination is found
        if target == 0:
            res.append(list(curr))
            return
    
        # Target is less than 0 or array is exhausted, return to 
        # explore other options
        if target < 0 or index >= len(arr):
            return

        # For all other combinations
        for i in range(index, len(arr)):
        
            # Check if it is repeated or not
            if i > index and arr[i] == arr[i - 1]:
                continue

            # Take the element into the combination
            curr.append(arr[i])

            # Recursive call
            self.findCombinations(arr, i + 1, target - arr[i], curr, res)

            # Remove element from the combination
            curr.pop()

    def uniqueCombinations(self, arr, target):
        # Sort the arr to handle duplicates
        arr.sort()
    
        # Final list where all unique combinations will be stored
        res = []
    
        # Store chosen elements in particular combination
        curr = []
    
        self.findCombinations(arr, 0, target, curr, res)
        return res