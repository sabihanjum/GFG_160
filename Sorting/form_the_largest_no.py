"""Given an array of integers arr[] representing non-negative integers, arrange them so that after concatenating all of them in order, it results in the largest possible number. Since the result may be very large, return it as a string."""

from functools import cmp_to_key

def my_compare(s1, s2):
    if s1 + s2 > s2 + s1:
        return -1
    else:
        return 1

class Solution:
    # Function to return the largest concatenated number
    def findLargest(self, arr):
        # Convert numbers to strings for comparison
        numbers = [str(ele) for ele in arr]
        
        # Sort the array using the custom comparator
        numbers.sort(key=cmp_to_key(my_compare))
        
        # Handle the case where all numbers are zero
        if numbers[0] == "0":
            return "0"
        
        # Concatenate the sorted numbers
        res = "".join(numbers)
        return res

