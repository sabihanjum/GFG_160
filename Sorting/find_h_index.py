"""Given an integer array citations[], where citations[i] is the number of citations a researcher received for the ith paper. The task is to find the H-index.

H-Index is the largest value such that the researcher has at least H papers that have been cited at least H times."""

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        n = len(citations)
        freq = [0]*(n+1)
        
        #count the  frequency of citations
        for citation in citations:
            if citation >= n:
                freq[n] += 1
            else:
                freq[citation] += 1
        idx = n
        
        #variable to keep track of the count of paper
        #having atleast idx citations
        s = freq[n]
        while s < idx:
            idx -= 1
            s += freq[idx]
            
        #return the largest index fr which the count of 
        #paper with at least idx cittaions bevome >= idx
        return idx