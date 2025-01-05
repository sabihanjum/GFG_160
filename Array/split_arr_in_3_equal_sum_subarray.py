"""Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false."""
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        res = []
        total = 0
        
        for ele in arr:
            total += ele
            
        #if the total sum is not divisible by 3
        #it is impossible to split the array
        if total % 3 != 0:
            res = [-1. -1]
            return res
            
        #keep track of the sum of current segment
        currSum = 0
        for i in range(len(arr)):
            currSum += arr[i]
            
            #if valid segment is found stores it index
            #and reset current sum to zero
            if currSum == total / 3:
                currSum = 0
                res.append(i)
                
                #if two valid segments are found and third
                #non empty segmentis possible, retutn index pair
                if len(res) == 2 and i < len(arr) - 1:
                    return res
        #if no index pair is possible
        res = [-1, -1]
        return res


