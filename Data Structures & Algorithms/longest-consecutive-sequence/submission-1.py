class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        comp = set(nums)
        max_length = 0
        for num in nums:
            if num-1 not in comp:
                length = 0
                while num+length in comp:
                    length +=1
                max_length = max(length,max_length)
        return max_length
        