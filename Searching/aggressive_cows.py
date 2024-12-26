"""You are given an array with unique elements of stalls[], which denote the position of a stall. You are also given an integer k which denotes the number of aggressive cows. Your task is to assign stalls to k cows such that the minimum distance between any two of them is the maximum possible."""

def check(stalls, k, dist):
    # Place the first cow at the first stall
    cnt = 1
    prev = stalls[0]
    
    # Iterate through the stalls to place cows
    for i in range(1, len(stalls)):
        # If the current stall is at least `dist` away from the last placed cow
        if stalls[i] - prev >= dist:
            cnt += 1
            prev = stalls[i]
        # If all cows are placed, return True
        if cnt == k:
            return True
            
    return False  # Not able to place all cows

class Solution:
    def aggressiveCows(self, stalls, k):
        # Sort the stalls to consider them in increasing order
        stalls.sort()
        res = 0
        
        # Define the search space for binary search
        lo = 1  # Minimum possible distance
        hi = stalls[-1] - stalls[0]  # Maximum possible distance
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            # If the current distance `mid` is feasible
            if check(stalls, k, mid):
                res = mid  # Update result with the feasible distance
                lo = mid + 1  # Search for a larger distance
            else:
                hi = mid - 1  # Search for a smaller distance
        
        return res
