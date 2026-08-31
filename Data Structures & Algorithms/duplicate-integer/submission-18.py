class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for n in nums:
            if n in hm:
                return True
            hm[n] = hm.get(n,0) + 1
        return False
        