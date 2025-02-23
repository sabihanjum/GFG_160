"""Given a string s consisting of opening and closing parenthesis '(' and ')'. Find the length of the longest valid parenthesis substring.

A parenthesis string is valid if:

For every opening parenthesis, there is a closing parenthesis.
The closing parenthesis must be after its opening parenthesis."""

class Solution:
    def maxLength(s):
        stack = []

        # Push -1 as the initial index to 
        # handle the edge case
        stack.append(-1)
        maxLen = 0

        # Traverse the string
        for i in range(len(s)):

            # If we encounter an opening parenthesis,
            # push its index
            if s[i] == '(':
                stack.append(i)
            else:

                # If we encounter a closing parenthesis, 
                # pop the stack
                stack.pop()

                # If stack is empty, push the current index
                # as a base for the next valid substring
                if not stack:
                    stack.append(i)
                else:
                    # Update maxLength with the current length 
                    # of the valid parentheses substring
                    maxLen = max(maxLen, i - stack[-1])

        return maxLen