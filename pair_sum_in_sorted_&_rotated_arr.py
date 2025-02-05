"""Given an array of positive elements arr[] that is sorted and then rotated around an unknown point, the task is to check if the array has a pair with sum equals to a given target."""

class Solution:
    ##Complete this function
    def pairInSortedRotated(self,arr, target):
        #Your code here
        n = len(arr)
        i = 0
        
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                break
            
        if arr[i] <= arr[i+1]:
            i+=1
    
        r = i
        l = (i+1)%n
        
        while l!=r:
            if arr[l]+arr[r] == target:
                return True
                
            if arr[l]+arr[r] < target:
                l = (l+1)%n
                
            else:
                r = (r-1+n)%n
        return False