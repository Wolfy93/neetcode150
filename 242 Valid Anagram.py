from collections import defaultdict

# Neetcode Link to problem: https://neetcode.io/problems/is-anagram?list=neetcode150
# Leetcode Link to problem: https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # I can think of two approaches
        # we can sort and compare. Complexity would be nlogn
        # we can create traverse and create a hashmap and compare those.

        chardict = defaultdict(int)
        if len(s) != len(t):
            return False
        else:
            for i in range(0,len(s)):
                    chardict[s[i]] += 1
                    chardict[t[i]] -= 1


        for val in chardict.values():
            if val!=0:
                return False
        
        return True
        
