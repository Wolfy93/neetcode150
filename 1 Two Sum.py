# Neetcode Problem Link: https://neetcode.io/problems/two-integer-sum?list=neetcode150
# Leetcode Problem Link: https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initial Thoughts
        # brute force: traverse array, for arr[i] check if target - arr[i]
        # exist in remaining array. Complexity = n sq
        #  But if we first sort and then search using binary search
        # The complexity can drop to nlogn but space will be O(n)
        # Optimal Approach: use dict to store element as key and its 
        # index as value

        numdict = dict()

        for i in range(len(nums)):
            if target - nums[i] in numdict:
                return [i, numdict[target - nums[i]]]
            else:
                numdict[nums[i]] = i 
        
