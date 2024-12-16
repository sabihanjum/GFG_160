"""Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return '$'.
Note: When you return '$' driver code will output -1."""

MAX_CHAR = 26
class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonRepeatingChar(self,s):
        vis = [-1]*MAX_CHAR
        
        #Iterate through the string
        for i in range(len(s)):
            #if character is seen for the first time store it index
            if vis[ord(s[i]) - ord('a')] == -1:
                vis[ord(s[i]) - ord('a')] = i
            
            #if character is seen again mark it as -2
            else:
                vis[ord(s[i]) - ord('a')] = -2
        idx = float('inf')
        
        #find the smallest index among all the non repeating character
        for i in range(MAX_CHAR):
            if vis[i] >= 0:
                idx = min(idx, vis[i])
                
        #if non repeating character is found return it else return '$'
        return '$' if idx == float('inf') else s[idx]