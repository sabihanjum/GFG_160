"""Given an array of strings, return all groups of strings that are anagrams. The strings in each group must be arranged in the order of their appearance in the original array. Refer to the sample case for clarification."""

from collections import defaultdict
class Solution:

    def anagrams(self, arr):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''

        ans = defaultdict(list)
        for s in arr:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
                
        return list(ans.values())