"""Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular."""

# Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    n = len(arr)
    
    # Helper function to compute max subarray sum using Kadane's algorithm
    def kadane(array):
        max_ending_here = max_so_far = array[0]
        for i in range(1, len(array)):
            max_ending_here = max(array[i], max_ending_here + array[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    
    # Step 1: Find the maximum subarray sum using Kadane's algorithm
    max_kadane = kadane(arr)
    
    # Step 2: Find the minimum subarray sum using Kadane's algorithm on the negated array
    total_sum = sum(arr)
    for i in range(n):
        arr[i] = -arr[i]
    min_kadane = -kadane(arr)  # Negate again to get the minimum sum
    
    # Step 3: Find the maximum circular sum
    if total_sum == min_kadane:  # Special case: all numbers are negative
        return max_kadane
    
    max_circular = max(max_kadane, total_sum - min_kadane)
    
    return max_circular
