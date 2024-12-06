"""You are given an array of integer arr[] where each number represents a vote to a candidate. Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return an empty array. 

Note: The answer should be returned in an increasing format"""

# moores voting algorithm

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        
        #Initialize two candidates and their counts
        ele1, ele2 = -1, -1
        cnt1, cnt2 = 0, 0
        
        for ele in arr:
            #increment count for candidate 1
            if ele1 == ele:
                cnt1 += 1
            #increment count for candidate 2
            elif ele2 == ele:
                cnt2 += 1
            #new candidate 1 if count is zero
            elif cnt1 == 0:
                ele1 = ele
                cnt1 += 1
            #new candidate 2 if count is zero
            elif cnt2 == 0:
                ele2 = ele
                cnt2 += 1
            #decrease count if neither candidates
            else:
                cnt1 -= 1
                cnt2 -= 1
        res = []
        cnt1, cnt2 = 0, 0
        
        #count the occurrence of candidates
        for ele in arr:
            if ele1 == ele:
                cnt1 += 1
            if ele2 == ele:
                cnt2 += 1
        
        #add to result if they are majority elements
        if cnt1 > n/3:
            res.append(ele1)
        if cnt2 > n / 3 and ele1 != ele2:
            res.append(ele2)
            
        if len(res) == 2 and res[0] > res[1]:
            res[0], res[1] = res[1], res[0]
            
        return res
