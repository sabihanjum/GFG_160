"""Given two sorted arrays a[] and b[] of size n and m respectively, the task is to merge them in sorted order without using any extra space. Modify a[] so that it contains the first n elements and modify b[] so that it contains the last m elements."""
class Solution:
    def mergeArrays(self, a, b):
        n = len(a)  # Length of first array
        m = len(b)  # Length of second array
        gap = (n + m + 1) // 2  # Initial gap size using the formula

        # Continue until the gap becomes 0
        while gap > 0:
            i = 0  # Pointer for the first element
            j = gap  # Pointer for the element at 'gap' distance

            while j < n + m:
                # If both pointers are in the first array `a`
                if j < n and a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]

                # If the first pointer is in `a` and the second pointer is in `b`
                elif i < n and j >= n and a[i] > b[j - n]:
                    a[i], b[j - n] = b[j - n], a[i]

                # If both pointers are in the second array `b`
                elif i >= n and b[i - n] > b[j - n]:
                    b[i - n], b[j - n] = b[j - n], b[i - n]

                i += 1  # Move both pointers forward
                j += 1

            # If the current gap is 1, break the loop as arrays are merged
            if gap == 1:
                break

            # Recalculate the next gap size
            gap = (gap + 1) // 2
