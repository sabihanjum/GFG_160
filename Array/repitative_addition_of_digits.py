"""You are given a positive integer n, you need to add all the digits of n and create a new number. Perform this operation until the resultant number has only one digit in it. Return the final number obtained after performing the given operation."""

class Solution:
    def singleDigit(self, n):
    	#if given number is zero it's digit sum will be zero onnly
    	if n == 0:
            return 0
        #if results of modulu operation zero then, the digit sum is 9
        if n % 9 == 0:
            return 9
        return n %9