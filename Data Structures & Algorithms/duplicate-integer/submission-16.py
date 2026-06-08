class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Use a hashset and check the lengths
        if len(set(nums)) < len(nums):
            return True
        else:
            return False

        