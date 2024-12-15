"""Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros."""

def trimLeadingZeros(s):
    # Find the position of the first '1'
    firstOne = s.find('1')
    return s[firstOne:] if firstOne != -1 else "0"  # Return "0" if there are no '1's

class Solution:
    def addBinary(self, s1, s2):
        # Trim leading zeros from both binary strings
        s1 = trimLeadingZeros(s1)
        s2 = trimLeadingZeros(s2)

        n = len(s1)
        m = len(s2)

        # Ensure s1 is the longer string
        if n < m:
            s1, s2 = s2, s1
            n, m = m, n

        j = m - 1
        carry = 0
        result = []

        # Traverse both strings from the end
        for i in range(n - 1, -1, -1):
            # Current bit of s1
            bit1 = int(s1[i])
            bitSum = bit1 + carry

            # If there are remaining bits in s2, add them to the bitSum
            if j >= 0:
                # Current bit of s2
                bit2 = int(s2[j])
                bitSum += bit2
                j -= 1

            # Calculate the result bit and update carry
            bit = bitSum % 2
            carry = bitSum // 2

            # Append the current bit to the result
            result.append(str(bit))

        # If there's any carry left, add it to the result
        if carry > 0:
            result.append('1')

        # Join the result list to form the final binary string
        return ''.join(result[::-1])
