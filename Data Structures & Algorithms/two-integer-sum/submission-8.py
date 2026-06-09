class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,num in enumerate(nums):
            res = target -num
            if res in hm:
                return [hm[res],i]
            hm[num] = i
        