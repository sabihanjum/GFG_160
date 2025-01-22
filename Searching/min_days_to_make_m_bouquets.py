"""You have a row of flowers, where each flower blooms after a specific day. The array arr represents the blooming schedule: arr[i] is the day the flower at position i will bloom. To create a bouquet, you need to collect k adjacent bloomed flowers. Each flower can only be used in one bouquet.

Your goal is to find the minimum number of days required to make exactly m bouquets. If it is not possible to make m bouquets with the given arrangement, return -1."""

def check(arr, k, m, days):
    bouquets = 0 
    cnt = 0
    
    #itertae through the bloom days of flower
    for i in range(len(arr)):
        if arr[i] <= days:
            cnt += 1
        else:
            #if the current bloom day count greater
            #than days. update bouquets and reset count
            bouquets += cnt // k
            cnt = 0
    bouquets += cnt // k
    
    #check if current bouquets are greater than are equal
    #to the desired number of bouquets
    return bouquets >= m
    
class Solution:
    def minDaysBloom(self, m, k, arr):
        # Code here
        lo = 0
        hi = max(arr)
        res = -1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if check(arr, k, m, mid):
                #if the current mid is valid update the result and
                #adjust the search range
                res = mid 
                hi = mid - 1
            else:
                #if the current mid is not valid adjust the search
                lo = mid + 1
        return res