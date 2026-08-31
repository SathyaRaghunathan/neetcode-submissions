class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #solution using hashset
        contains = set()
        for n in nums:
            if n in contains:
                return True
            contains.add(n)
        return False
        