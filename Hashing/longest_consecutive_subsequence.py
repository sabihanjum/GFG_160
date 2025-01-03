"""Given an array arr[] of non-negative integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order."""

class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        s = set()
        ans = 0
        n = len(arr)
        
        #hash all the array element
        for ele in arr:
            s.add(ele)
            
        #check each possible element from the start
        #then update optimal length
        for i  in range(n):
            #if current element is the starting element of sequence
            if (arr[i]-1) not in s:
                #then check for next elemnt on sequence
                j = arr[i]
                while(j in s):
                    j += 1
                    
                #update optimal length if this length is more
                ans = max(ans, j-arr[i])
        return ans