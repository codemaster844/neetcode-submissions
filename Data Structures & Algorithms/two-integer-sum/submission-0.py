class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index=dict()
        for i in range(len(nums)):
            if target-nums[i] in index:
                return [index[target-nums[i]],i]
            else:
                index[nums[i]]=i