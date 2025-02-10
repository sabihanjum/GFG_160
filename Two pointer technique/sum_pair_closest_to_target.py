"""Given an array arr[] and a number target, find a pair of elements (a, b) in arr[], where a<=b whose sum is closest to target.
Note: Return the pair in sorted order and if there are multiple such pairs return the pair with maximum absolute difference. If no such pair exists return an empty array."""

class Solution:
    def sumClosest(arr, target):
        n = len(arr)
        arr.sort()
        res = []
        minDiff = float('inf')

        left = 0
        right = n - 1

        while left < right:
            currSum = arr[left] + arr[right]

            # Check if this pair is closer than the closest
            # pair so far
            if abs(target - currSum) < minDiff:
                minDiff = abs(target - currSum)
                res = [arr[left], arr[right]]

            # If this pair has less sum, move to greater values
            if currSum < target:
                left += 1

            # If this pair has more sum, move to smaller values
            elif currSum > target:
                right -= 1

            # If this pair has sum = target, return it
            else:
                return res

        return res