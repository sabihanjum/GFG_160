"""Given two strings, one is a text string txt and the other is a pattern string pat. The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
Note: Return an empty list in case of no occurrences of pattern."""

def constructLps(pat, lps):
    # len_ stores the length of the longest prefix
    # which is also a suffix for the previous index
    len_ = 0  # Length of the previous longest prefix suffix
    m = len(pat)

    # lps[0] is always 0
    lps[0] = 0

    i = 1
    while i < m:
        # If characters match, increment the size of the LPS
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            # If there is a mismatch
            if len_ != 0:
                # Update len_ to the previous LPS value
                # to avoid redundant comparisons
                len_ = lps[len_ - 1]
            else:
                # If no matching prefix is found, set lps[i] to 0
                lps[i] = 0
                i += 1


class Solution:
    def search(self, pat, txt):
        n = len(txt)  # Length of the text
        m = len(pat)  # Length of the pattern

        lps = [0] * m  # Array to store the LPS values
        res = []  # Result list to store the start indices of matches

        constructLps(pat, lps)  # Preprocess the pattern to get the LPS array

        # Pointers i and j for traversing the text and pattern
        i = 0  # Pointer for text
        j = 0  # Pointer for pattern

        while i < n:
            # If characters match, move both pointers forward
            if txt[i] == pat[j]:
                i += 1
                j += 1

                # If the entire pattern matches
                if j == m:
                    res.append(i - j)  # Store the start index in the result

                    # Use the LPS value of the previous index
                    # to skip unnecessary comparisons
                    j = lps[j - 1]

            # If there is a mismatch
            else:
                # Use the LPS value to avoid redundant comparisons
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1  # Move text pointer forward

        return res
