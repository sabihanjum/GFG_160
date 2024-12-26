"""Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array."""

class Solution:
    def kthElement(self, a, b, k):
        n = len(a)
        m = len(b)
        
        # Ensure `a` is the smaller array to reduce complexity
        if n > m:
            return self.kthElement(b, a, k)
        
        # Binary search on the smaller array
        lo = max(0, k - m)
        hi = min(k, n)
        
        while lo <= hi:
            mid1 = (lo + hi) // 2
            mid2 = k - mid1

            # Handle edge cases for partitions
            l1 = float('-inf') if mid1 == 0 else a[mid1 - 1]
            r1 = float('inf') if mid1 == n else a[mid1]
            l2 = float('-inf') if mid2 == 0 else b[mid2 - 1]
            r2 = float('inf') if mid2 == m else b[mid2]

            # Check for valid partition
            if l1 <= r2 and l2 <= r1:
                return max(l1, l2)

            # Adjust search range
            if l1 > r2:
                hi = mid1 - 1  # Move left
            else:
                lo = mid1 + 1  # Move right
        
        return -1  # Return -1 in case of failure (shouldn't happen with valid inputs)
