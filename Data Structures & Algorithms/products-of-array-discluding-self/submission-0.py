class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0]*n
        right_mul,left_mul = 1,1
        for i in range(n):
            #left side
            for l in range(0,i):
                left_mul *= nums[l]
            for r in range(i+1,n):
                right_mul *= nums[r]
            output[i] = left_mul*right_mul
            right_mul = left_mul =1
        return output