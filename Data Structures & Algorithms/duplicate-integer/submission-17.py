class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Use a hashset and check the lengths
        return len(set(nums))< len(nums)

        