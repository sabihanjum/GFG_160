"""Given a dictionary of words arr[] where each word follows CamelCase notation, print all words in the dictionary that match with a given pattern pat consisting of uppercase characters only.

CamelCase is the practice of writing compound words or phrases such that each word or abbreviation begins with a capital letter. Common examples include PowerPoint and Wikipedia, GeeksForGeeks, CodeBlocks, etc.

Example: "GeeksForGeeks" matches the pattern "GFG", because if we combine all the capital letters in "GeeksForGeeks" they become "GFG". Also note "GeeksForGeeks" matches with the pattern "GFG" and also "GF", but does not match with "FG".

Note: The driver code will sort your answer before checking and return the answer in any order."""

class Solution:
    def camelCase(self,arr,pat):
        #list for storing camel case
        res = []
        
        for word in arr:
            i, j = 0, 0
            while i < len(word) and j < len(pat):
                #if ith character of word is lowercase
                #character, move to next character
                if word[i].islower():
                    i += 1
                    
                #if ith character of word is an uppercase 
                #character and does not match with jth 
                #character of pattern, move to the next word
                elif word[i] != pat[j]:
                    break
                
                #if ith character of word is an uppercase 
                #character and match with jth character of
                #pattern move to the next character
                else:
                    i += 1
                    j += 1
            #if all character of the pattern matched
            #then insert the word in result
            if j == len(pat):
                res.append(word)
        return res