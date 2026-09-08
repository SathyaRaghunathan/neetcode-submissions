class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            local_longest = 0
            if num -1 not in numSet:
                local_longest +=1
                while (num+local_longest) in numSet:
                    local_longest+=1
                longest = max(longest,local_longest)
        return longest
                

        