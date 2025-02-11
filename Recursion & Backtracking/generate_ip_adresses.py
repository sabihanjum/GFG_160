"""Given a string s containing only digits, your task is to restore it by returning all possible valid IP address combinations. You can return your answer in any order.

A valid IP address must be in the form of A.B.C.D, where A, B, C, and D are numbers from 0-255(inclusive).

Note: The numbers cannot be 0 prefixed unless they are 0. For example, 1.1.2.11 and 0.11.21.1 are valid IP addresses while 01.1.2.11 and 00.11.21.1 are not."""

class Solution:
    # Function to check whether segment is valid or not.
    def isValid(s):
        n = len(s)

        # Segment of length one is always valid
        if n == 1:
            return True

        # Converting string into integer
        val = int(s)

        # Invalid case: If it has a preceding zero or 
        # its value is greater than 255
        if s[0] == '0' or val > 255:
            return False

        return True

    # Recursive helper function to generate valid IP address
    def generateIpRec(self, s, index, curr, cnt, res):
        temp = ""

        # Base case: Reached end of string and 
        # all 4 segments were not completed
        if index >= len(s):
            return

        if cnt == 3:
            temp = s[index:]

            # Checking 4th (last) segment of IP address
            if len(temp) <= 3 and self.isValid(temp):
                res.append(curr + temp)

            return

        for i in range(index, min(index + 3, len(s))):
            # Creating next segment of IP address
            temp += s[i]

            # If the created segment is valid
            if self.isValid(temp):
                # Generate the remaining segments of IP
                self.generateIpRec(s, i + 1, curr + temp + ".", cnt + 1, res)

    # Function to generate valid IP address
    def generateIp(self, s):
        res = []
        self.generateIpRec(s, 0, "", 0, res)
        return res