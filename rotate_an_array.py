"""Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps, where d is a positive integer. Do the mentioned change in the array in place.

Note: Consider the array as circular."""

#Juggling algorithm 
#reversal algorithm

class Solution:
    # Function to rotate an array by `d` elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        # Find the length of the array
        n = len(arr)
        
        # Handle cases where d > n by using modulo to reduce unnecessary rotations
        d %= n
        
        # Step 1: Reverse the first `d` elements
        reverse(arr, 0, d - 1)
        
        # Step 2: Reverse the remaining `n-d` elements
        reverse(arr, d, n - 1)
        
        # Step 3: Reverse the entire array
        reverse(arr, 0, n - 1)
        
# Helper function to reverse elements of an array between indices `start` and `end`
def reverse(arr, start, end):
    while start < end:
        # Swap the elements at `start` and `end`
        arr[start], arr[end] = arr[end], arr[start]
        
        # Move the pointers closer
        start += 1
        end -= 1

