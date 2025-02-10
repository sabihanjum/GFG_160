"""Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k."""

class Solution:
    def countTriplets(self, arr, target):
        res = 0
        n = len(arr)
        
        for i in range(n-2):
            left = i + 1
            right = n - 1
            
            while left < right:
                sum = arr[i] + arr[left] + arr[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    if arr[left] == arr[right]:
                        count = right - left + 1
                        res += (count * ( count-1)) // 2
                        break
                    else:
                        
                        ele1 = arr[left]
                        ele2 = arr[right]
                        cnt1 = 0
                        cnt2 = 0
                    
                        while left <= right and arr[left] == ele1:
                            left += 1
                            cnt1 += 1
                    
                        while left <= right and arr[right] == ele2:
                            right -= 1
                            cnt2 += 1
                        res += (cnt1 * cnt2)
                            
        return res