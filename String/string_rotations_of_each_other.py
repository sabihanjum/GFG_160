"""You are given two strings of equal lengths, s1 and s2. The task is to check if s2 is a rotated version of the string s1.

Note: The characters in the strings are in lowercase."""

def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n
    
    #length of the previous longest suffix
    patLen = 0
    
    #lps[0] is always zero
    lps[0] = 0
    
    #loops calculatelps[i] for i-1 to n - 1
    i = 1
    while i < n:
        #if character matches, increment len 
        #and exchange matching prefix
        if pat[i] == pat[patLen]:
            patLen += 1
            lps[i] = patLen
            i +=  1
        #if there is mismatch
        else:
            #if len is not zero update len to the last known
            #prefix length
            if patLen != 0:
                patLen = lps[patLen - 1]
            #no prefix matches set lps[i] to zero
            #and move to the next character
            else:
                lps[i] = 0
                i += 1
    return lps

class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        # s1 = s1 + s1
        # #find s2 in concatenated string
        # return s2 in s1
        
        txt = s1 + s1
        pat = s2
        
        #search the pattern string s2 in concatination string
        n = len(txt)
        m = len(pat)
        
        #create lps[] that will hold the longest prefix
        #suffix value for pattern
        lps = computeLPSArray(pat)
        
        i = 0
        j = 0
        while i < n:
            if pat[j] == txt[i]:
                j += 1
                i += 1
            if j == m:
                return True
                
            #mismatch after j matches
            elif i < n and pat[j] != txt[i]:
                #Do not match lps[0...lps[j-1]] character
                #they will match anyway
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False