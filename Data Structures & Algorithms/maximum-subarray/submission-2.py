class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxSum=-float('inf')
        sumtemp=0
        for i in nums:
            if sumtemp<0:
                sumtemp=0
            sumtemp+=i
            maxSum=max(sumtemp,maxSum)
        return maxSum