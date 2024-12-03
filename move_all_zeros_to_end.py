"""Given an array arr[]. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in place."""

class Solution:
    def pushZerosToEnd(self, arr):
        
        count = 0  # Count of non-zero elements (also the index where the next non-zero element will be placed)

        # Traverse the array
        for i in range(len(arr)):
            if arr[i] != 0:  # If the current element is non-zero
                # Swap the current element with the element at index `count`
                arr[i], arr[count] = arr[count], arr[i]
                count += 1  # Increment the count to move to the next position for non-zero elements
