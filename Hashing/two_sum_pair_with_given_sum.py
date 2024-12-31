"""Given an array arr[] of positive integers and another integer target. Determine if there exists two distinct indices such that the sum of there elements is equals to target."""

class Solution:
    def twoSum(self, arr, target):
        # Create a set to store the elements we've seen
        seen = set()
        
        # Iterate through each element in the array
        for num in arr:
            # Calculate the complement that, when added to num, equals the target
            complement = target - num
            
            # Check if the complement exists in the set
            if complement in seen:
                return True  # Pair found
            
            # Add the current element to the set
            seen.add(num)
        
        # If no pair is found, return False
        return False
