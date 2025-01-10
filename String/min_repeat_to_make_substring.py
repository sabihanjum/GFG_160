"""Given two strings s1 and s2. Return a minimum number of times s1 has to be repeated such that s2 is a substring of it. If s2 can never be a substring then return -1.

Note: Both the strings contain only lowercase letters."""

class Solution:
    def computeLPSArray(s):
        lps = [0] * len(s)
        len_ = 0
        idx = 1

        # the loop calculates lps[i] for
        # i = 1 to str.length() - 1
        while idx < len(s):
            if s[idx] == s[len_]:
                len_ += 1
                lps[idx] = len_
                idx += 1
            else:
            
                # If len is 0, then we have no common prefix
                # which is also a suffix
                if len_ == 0:
                    lps[idx] = 0
                    idx += 1
                else:
                
                    # Note that we do not move to the next index
                    len_ = lps[len_ - 1]
        return lps

# function to find the occurrence of pat in txt

def KMPSearch(txt, pat, lps):
    n, m = len(txt), len(pat)
    i = j = 0

    # Iterate till s1 is repeated rep times
    while i < n:
        
        # If characters match, move both pointers forward
        if txt[i] == pat[j]:
            i += 1
            j += 1

            # If the entire pattern is matched
            if j == m:
                return True
                
                # Use lps of previous index to skip 
                # unnecessary comparisons
                j = lps[j - 1]
        else:
            
            # If there is a mismatch, use lps value of 
            # previous index to avoid redundant comparisons
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return False

# function to find Minimum number of times s1 has to be
# repeated such that s2 is a substring of it

def minRepeats(s1, s2):
    
    # Find lengths of strings
    n, m = len(s1), len(s2)

    # Declare and Compute the LPS Table
    lps = computeLPSArray(s2)

    # Find the minimum number of times s1 needs to be
    # repeated to become as long as s2
    x = (m + n - 1) // n

    text = s1 * x
    
    # Check when string s1 is repeated x times
    if KMPSearch(text, s2, lps):
        return x

    text += s1
    # Check when string s1 is repeated (x + 1) times
    if KMPSearch(text, s2, lps):
        return x + 1

    # If string s2 was not found, return -1
    return -1