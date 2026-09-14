class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_det,post_det = 1,1
        output = [1]*len(nums)
        #left to right
        for i in range(len(nums)):
            output[i] *= pre_det
            pre_det *= nums[i]
        #right to left
        for i in range(len(nums)-1,-1,-1):
            output[i] *= post_det
            post_det *= nums[i]
        
        return output

