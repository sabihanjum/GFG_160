"""We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.
When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time. When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left[] and right[], the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank."""

class Solution:
    def getLastMoment(self, n, left, right):
        res = 0
        
        #find the time to fall off the plank for all
        #ants moving towards left
        for i in range(len(left)):
            res = max(res, left[i])
            
        #find the time to fall off the plank for all
        #ants moving towards right
        for i in range(len(right)):
            res = max(res, n - right[i])
            
        #return the maximum time among all ants
        return res