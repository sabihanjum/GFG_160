"""Fizz Buzz Problem involves that given an integer n, for every integer 0 < i <= n, the task is to output,

"FizzBuzz" if i is divisible by 3 and 5,
"Fizz" if i is divisible by 3,
"Buzz" if i is divisible by 5
"i" as a string, if none of the conditions are true.
Return an array of strings."""

class Solution:
    def fizzBuzz(self, n : int):
        
        res = []
        
        #dictionary to  store all fizzBuzz mappings
        mp = {3: "Fizz", 5: "Buzz"}
        divisors = [3, 5]
        
        for i in range(1, n+1):
            s = ""
            
            for d in divisors:
                #if the i is divisible by d, add
                #corresponding string map wuth d
                if i % d == 0:
                    s += mp[d]
                    
            #not divisible by 3 or 5 add the number
            if not s:
                s += str(i)
                
            #append the corrent answer str to the resultant list
            res.append(s)
            
        return res