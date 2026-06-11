class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        for num in nums:
            hm[num]+=1
        
        sorted_hm = dict(sorted(hm.items(), key = lambda x:x[1], reverse = True))
        output = [k for k,v in sorted_hm.items()]
        return output[:k]