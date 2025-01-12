"""Write a function to convert a given number n into words.

The idea is to break down the number into International Number System, i.e., smaller groups of three digits (hundreds, tens, and ones), and convert each group into words."""

class Solution:
    def convertToWords(self, n):
        if n == 0:
            return "Zero"
            
        #words for number zero to 19
        units = ["",     "One",   "Two",    "Three",
                "Four", "Five",   "Six",   "Seven",
                "Eight", "Nine",   "Ten",   "Eleven",
                "Twelve", "Thirteen", "Fourteen", "Fifteen",
                "Sixteen", "Seventeen", "Eighteen", "Nineteen"
                ]
        #words for number multiple of 10
        tens = ["",      "",      "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
                ]
                
        multiplier = ["", "Thousand", "Million", "Billion"]
        
        res = ""
        group = 0
        
        #process number in group of thousands
        while n > 0:
            if n % 1000 != 0:
                value = n % 1000
                temp = ""
                
                #handle 3 digit number
                if value >= 100:
                    temp = units[value//100] + " Hundred "
                    value %= 100
                    
                #handle 2 digit number
                if value >= 20:
                    temp += tens[value//10] + " "
                    value %= 10
                    
                #handle unit number
                if value > 0:
                    temp += units[value] + " "
                    
                #add the multiplier according to group
                temp += multiplier[group] + " "
                
                #add the result of this group to overall result
                res = temp + res
            n //= 1000
            group += 1
        #remove trailing space
        return res.strip()