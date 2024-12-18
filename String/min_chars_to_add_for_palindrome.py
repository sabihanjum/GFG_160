"""Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.

Note: A palindrome string is a sequence of characters that reads the same forward and backward."""

def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n
    
    #lps[0] is always zero
    len_lps = 0
    
    #loops calculatelps[i] for i-1 to n - 1
    i = 1
    while i < n:
        #if character matches, increment len n set lps[i]
        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i +=  1
        #if there is mismatch
        else:
            #if len is not zero update len to the last known
            #prefix length
            if len_lps != 0:
                len_lps = lps[len_lps - 1]
            #no prefix matches set lps[i] to zero
            else:
                lps[i] = 0
                i += 1
    return lps
        

class Solution:
    def minChar(self, s):
        n = len(s)
        rev = s[::-1]
        
        #get concatenation of string, special character
        #and reverse string
        s = s + '$' + rev
        
        #get LPS array of this concatenating string
        lps = computeLPSArray(s)
        
        #By subtracting last entry of lps array from
        #string length will get our result
        return n - lps[-1]