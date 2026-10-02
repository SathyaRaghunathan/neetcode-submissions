class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        li = 1
        ri = 1
        for i in range(len(nums)):
            output[i] *= li
            li *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i]*= ri
            ri *= nums[i]
        return output