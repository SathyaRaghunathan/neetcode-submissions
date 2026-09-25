class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for num in nums:
            hm[num] = 1+ hm.get(num,0)
        for key,val in hm.items():
            if val >1:
                return True
        return False