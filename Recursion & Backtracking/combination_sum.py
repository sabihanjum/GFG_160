"""Given an array arr[] and a target, your task is to find all unique combinations in the array where the sum is equal to target. The same number may be chosen from the array any number of times to make target.

You can return your answer in any order."""

class Solution:
    def makeCombination(self, arr, remSum, cur, res, index):

        # If remSum is 0 then add the combination to the result
        if remSum == 0:
            res.append(list(cur))
            return

        # Invalid Case: If remSum is less than 0 or if index >= len(arr)
        if remSum < 0 or index >= len(arr):
            return

        # Add the current element to the combination
        cur.append(arr[index])

        # Recur with the same index
        self.makeCombination(arr, remSum - arr[index], cur, res, index)

        # Remove the current element from the combination
        cur.pop()

        # Recur with the next index
        self.makeCombination(arr, remSum, cur, res, index + 1)

    # Function to find all combinations of elements
    # in array arr that sum to target.
    def combinationSum(self, arr, target):
        arr.sort()

        # List to store combinations
        cur = []

        # List to store valid combinations
        res = []
        self.makeCombination(arr, target, cur, res, 0)
    
        return res