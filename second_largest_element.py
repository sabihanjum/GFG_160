"""Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element."""

class Solution:
    def getSecondLargest(self, arr):
        
        n = len(arr)

        # If the array has fewer than 2 elements, the second largest doesn't exist
        if n < 2:
            return -1

        # Initialize the largest (`first`) and second largest (`second`) as negative infinity
        first = second = float('-inf')

        # Traverse through the array
        for num in arr:
            if num > first:  # Found a new largest number
                second = first  # Update second largest
                first = num  # Update largest
            elif num > second and num != first:  # Found a new second largest
                second = num

        # If no second largest value was found, return -1
        if second == float('-inf'):
            return -1
        else:
            return second
