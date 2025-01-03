"""Given two integer arrays a[] and b[], you have to find the intersection of the two arrays. Intersection of two arrays is said to be elements that are common in both arrays. The intersection should not have duplicate elements and the result should contain items in any order.

Note: The driver code will sort the resulting array in increasing order before printing."""

class Solution:
    def intersectionWithDuplicates(self, a, b):
        # put all the element of a[] in sa
        sa = set(a)
        res = []
        
        #traverse through b[]
        for elem in b:
            #if the element is in sa
            if elem in sa:
                res.append(elem) #add it to the result arr
                sa.remove(elem) #erase it from sa to avoid duplicates

        return res
