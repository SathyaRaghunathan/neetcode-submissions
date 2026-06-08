class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Lets try sorting it
        nums.sort()
        for cur_val,next_val in zip(nums,nums[1:]):
            if cur_val == next_val:
                return True
        return False


        