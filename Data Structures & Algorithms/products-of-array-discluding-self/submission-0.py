class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]*len(nums)
        right=[1]*len(nums)
        mul=1
        ans=[]

        for i in range(len(nums)):
            left[i]=mul
            mul*=nums[i]
        mul=1
        for i in range(len(nums)-1,-1,-1):
            right[i]=mul
            mul*=nums[i]
        for i in range(len(nums)):
            sol=(left[i]*right[i])
            ans.append(sol)
        return ans

        


        