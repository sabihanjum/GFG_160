"""Given an array arr[], the task is to reverse the array. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on."""

class Solution:
    def reverseArray(self, arr):
        # Get the length of the array
        n = len(arr)
        
        # Loop to iterate through the first half of the array
        for i in range(n // 2):
            # Store the current element in a temporary variable
            temp = arr[i]
            
            # Swap the element at the current index with the corresponding element
            # from the other end of the array
            arr[i] = arr[n - i - 1]
            arr[n - i - 1] = temp
