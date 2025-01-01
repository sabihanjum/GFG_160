"""Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct."""

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def findUnion(self, a, b):
        st = set()
        
        #put all the elements of a[] in st
        for i in range(len(a)):
            st.add(a[i])
            
        #put all the elements of b[] in st
        for i in range(len(b)):
            st.add(b[i])
            
        res = []
        
        #iterate through set to fill the result array
        for it in st:
            res.append(it)
        return len(res)