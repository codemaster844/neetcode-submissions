class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxLen=0
        for i in numSet:
            if (i-1) not in numSet:
                longest=1
                while (i+longest) in numSet:
                    longest+=1
                maxLen=max(maxLen,longest)
        return maxLen
        