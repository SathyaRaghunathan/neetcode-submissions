class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num] +=1
        shm = dict(sorted(hm.items(),key=lambda x:x[1],reverse = True))
        return list(shm.keys())[:k]