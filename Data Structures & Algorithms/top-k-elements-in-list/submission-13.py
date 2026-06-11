class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = dict(Counter(nums))
        shm = dict(sorted(hm.items(),key = lambda x:x[1],reverse = True))
        return list(shm.keys())[:k]
        
        