class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visit = {}
        for num in nums:
            visit[num] = 1 + visit.get(num,0)
        
        for val in visit.values():
            if val>1:
                return True
        return False