"""Given a string s, the objective is to convert it into integer format without utilizing any built-in functions. Refer the below steps to know about atoi() function.

Cases for atoi() conversion:

Skip any leading whitespaces.
Check for a sign (‘+’ or ‘-‘), default to positive if no sign is present.
Read the integer by ignoring leading zeros until a non-digit character is encountered or end of the string is reached. If no digits are present, return 0.
If the integer is greater than 231 – 1, then return 231 – 1 and if the integer is smaller than -231, then return -231."""

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        res = 0
        idx = 0
        
        # Ignore leading whitespace
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        
        # Check for optional '+' or '-' sign
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                sign = -1
            idx += 1
        
        # Construct the number digit by digit
        while idx < len(s) and '0' <= s[idx] <= '9':
            res = 10 * res + (ord(s[idx]) - ord('0'))
            
            # Check for overflow/underflow
            if res > (2**31 - 1):
                return (2**31 - 1) if sign == 1 else -2**31
            
            idx += 1
        
        return res * sign
