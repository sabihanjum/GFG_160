"""Given a string of characters s, find the length of the longest prefix which is also a suffix.
Note: Prefix and suffix can be overlapping but they should not be equal to the entire string."""

# Python program to find the length of longest proper prefix
# that is also suffix using lps of KMP Algorithm

class Solution:
    def longestPrefixSuffix(s):
        n = len(s)
        lps = [0] * n
    
        # len stores the length of longest prefix which
        # is also a suffix for the previous index
        length = 0

        # lps[0] is always 0
        lps[0] = 0

        i = 1
        while i < n:

            # If characters match, increment the size of lps
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            # If there is a mismatch
            else:
                if length != 0:

                    # Update length to the previous lps value
                    # to avoid redundant comparisons
                    length = lps[length - 1]
                else:
                    # If no matching prefix found, set lps[i] to 0
                    lps[i] = 0
                    i += 1
    
        # Last element of lps array will store the length of
        # longest prefix that is also suffix of entire string
        return lps[n - 1]

