"""Given a string s, find the length of the longest substring with all distinct characters."""

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        res = 0
        
        lastIndex = [-1] * 26
        
        start = 0
        
        for end in range(n):
            start = max(start, lastIndex[ord(s[end]) - ord('a')]+1)
            res = max(res, end - start + 1)
            
            lastIndex[ord(s[end])-ord('a')] = end
        return res