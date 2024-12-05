"""Given an array of integers arr[] representing a permutation, implement the next permutation that rearranges the numbers into the lexicographically next greater permutation. If no such permutation exists, rearrange the numbers into the lowest possible order (i.e., sorted in ascending order). 

Note - A permutation of an array of integers refers to a specific arrangement of its elements in a sequence or linear order."""

class Solution:
    def nextPermutation(self, arr):
        # Find the length of the array
        n = len(arr)

        # Step 1: Find the first decreasing element from the right (pivot point)
        pivot = -1
        for i in range(n - 2, -1, -1):  # Start from the second-last element
            if arr[i] < arr[i + 1]:  # Check if the current element is less than the next element
                pivot = i
                break

        # Step 2: If no pivot was found, the array is in descending order. Reverse it to get the smallest permutation.
        if pivot == -1:
            arr.reverse()
            return

        # Step 3: Find the smallest number greater than arr[pivot] to the right of pivot
        for i in range(n - 1, pivot, -1):  # Start from the end of the array
            if arr[i] > arr[pivot]:  # Find the first element larger than arr[pivot]
                # Swap arr[i] and arr[pivot]
                arr[i], arr[pivot] = arr[pivot], arr[i]
                break

        # Step 4: Reverse the elements to the right of the pivot to get the next permutation
        left, right = pivot + 1, n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


