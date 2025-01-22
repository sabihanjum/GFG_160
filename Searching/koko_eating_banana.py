"""Given an array arr[] of integers where each element represents a pile of bananas, and Koko has k hours to finish all the piles, find the minimum number of bananas (s) Koko must eat per hour to finish all the bananas within k hours. Each hour, Koko chooses a pile and eats s bananas from it. If the pile has fewer than s bananas, she consumes the entire pile for that hour and won't eat any other banana during that hour."""

def check(arr, mid, k):
    hours = 0
    for bananas in arr:
        hours += bananas // mid
            
        #1 extra hour to eat the remainder number
        #of bananas in this pile
        if bananas % mid != 0:
            hours += 1
                
    #return true if given time is lexx than or equal
    #to given hours, or else return false
    return hours <= k
        
class Solution:
    def kokoEat(self,arr,k):
        #minimum speed of eating 1 banana/hour
        lo = 1
        
        #maximum speed of eating is the max banana in given pile
        hi = max(arr)
        res = hi
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            #check if the mid of hours is valid
            if check(arr, mid, k):
                #if valid continue to serach at lower speed
                hi = mid - 1
                res = mid
            else:
                #if can't finish bananas in given hour
                #then increase the speed
                lo = mid + 1
                
        return res