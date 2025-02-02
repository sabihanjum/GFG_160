"""Given an array arr[] of integers and another integer target. Find all unique quadruples from the given array that sums up to target.

Note: All the quadruples should be internally sorted, ie for any quadruple [q1, q2, q3, q4] it should be : q1 <= q2 <= q3 <= q4."""

class Solution:
    def fourSum(self, arr, target):
        # code here
        res = []
        n = len(arr)
        arr.sort()
        
        for i in range(n-3):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1, n-2):
                if j>i+1 and arr[j]==arr[j-1]:
                    continue
                k=j+1
                l=n-1
                
                while k<l:
                    sum=arr[i]+arr[j]+arr[k]+arr[l]
                    if sum==target:
                        res.append([arr[i], arr[j], arr[k], arr[l]])
                        k+=1
                        l-=1
                        
                        while k<l and arr[k]==arr[k-1]:
                            k+=1
                        while k<l and arr[l]==arr[l+1]:
                            l-=1
                    elif sum<target:
                        k+=1
                    else:
                        l-=1
        return res