"""Given a string s with repeated characters, the task is to rearrange characters in a string such that no two adjacent characters are the same.
Note: The string has only lowercase English alphabets and it can have multiple solutions. Return any one of them. If there is no possible solution, then print empty string ("")."""

from collections import Counter
import heapq
class Solution:

    def rearrangeString(s):
        n = len(s)
    
        # Store frequencies of all characters in string
        freq = Counter(s)
    
        # Insert all characters with their frequencies
        # into a max heap
        pq = [(-value, key) for key, value in freq.items()]
        heapq.heapify(pq)
    
        res = []
        prev = (0, '')  # previous character and its remaining count
    
        while pq:
            # Pop top element from queue and add it
            # to string.
            count, char = heapq.heappop(pq)
            res.append(char)
        
            # If frequency of previous character is less
            # than zero that means it is useless, we
            # need not to push it
            if prev[0] < 0:
                heapq.heappush(pq, prev)
        
            # Make current character as the previous 'char'
            # decrease frequency by 'one'
            prev = (count + 1, char)
    
        # If length of the resultant string and original
        # string is not same then string is not valid
        if len(res) != n:
            return ""
    
        # Valid String
        return "".join(res)