# Problem Description Link: https://neetcode.io/problems/duplicate-integer?list=neetcode150
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numset = set()
        for i in nums:
            if i in numset:
                return True
            else:
                numset.add(i)
        return False
