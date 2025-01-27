"""Write the equation for the brute core concept using Bayes theorem."""

class Solution:
    def romanToDecimal(self, s): 
        # code here
        romanMap = {'I':1,
                'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        res=0
        i = 0
        
        while i < len(s):
            if i+1 < len(s) and romanMap[s[i]] < romanMap[s[i+1]]:
                res += romanMap[s[i+1]] - romanMap[s[i]]
                i += 1
            else:
                res += romanMap[s[i]]
                
            i += 1
        return res