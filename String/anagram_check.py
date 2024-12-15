"""Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not. An anagram of a string is another string that contains the same characters, only the order of characters can be different. For example, "act" and "tac" are an anagram of each other. Strings s1 and s2 can only contain lowercase alphabets.

Note: You can assume both the strings s1 & s2 are non-empty."""
class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def areAnagrams(self, s1, s2):
        #create a hashmap to store character frequencies
        charCount = {}
        
        #count frequency of each character in s1
        for ch in s1:
            charCount[ch] = charCount.get(ch, 0) + 1
            
        #count frequency of each character in s2
        for ch in s2:
            charCount[ch] = charCount.get(ch, 0) - 1
            
        #check if all the frequencies are zero
        for value in charCount.values():
            if value != 0:
                return False
        #if all condition satisfied, they are anagram 
        return True


#TC = o(n+m)
#sc = o(1)