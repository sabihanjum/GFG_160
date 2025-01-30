"""Given an array of strings (all lowercase letters), the task is to group them in such a way that all strings in a group are shifted versions of each other.

Two strings s1 and s2 are called shifted if the following conditions are satisfied:

s1.length = s2.length
s1[i] = s2[i] + m for 1 <= i <= s1.length  for a constant integer m"""

def getHash(s):
    hashVal = []
        
    shift = ord(s[0])-ord('a')
        
    for ch in s:
        newCh = chr(ord(ch)-shift)
            
        if newCh < 'a':
            newCh = chr(ord(newCh)+26)
        hashVal.append(newCh)
    return ''.join(hashVal)
class Solution:
    
            
    def groupShiftedString(self, arr):
        #code here
        res = []
        mp = {}
        
        for i in range(len(arr)):
            hashVal = getHash(arr[i])
            
            if hashVal not in mp:
                mp[hashVal] = len(res)
                res.append([])
            res[mp[hashVal]].append(arr[i])
        return res