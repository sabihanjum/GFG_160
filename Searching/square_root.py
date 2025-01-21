"""Given a positive integer n, find the square root of n. If n is not a perfect square, then return the floor value.

Floor value of any number is the greatest Integer which is less than or equal to that number"""

class Solution:
    def floorSqrt(self, n): 
        #initial serach space
        lo = 1
        hi = n
        res = 1
        
        while lo <= hi:
            mid = lo + (hi - lo)//2
            
            #if the square of mid less than or equal to n
            #update the result and search in upper half
            if mid * mid <= n:
                res = mid
                lo = mid + 1
                
            #if square of mid exceed n serach in lower half
            else:
                hi = mid - 1
        return res
    