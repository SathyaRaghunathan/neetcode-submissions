class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        hm = {}
        ll = [[] for i in range(len(nums)+1)]
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        
        for num,cnt in hm.items():
            ll[cnt].append(num)
        
        result = []
        for i in range(len(ll)-1,-1,-1):
            for num in ll[i]:
                result.append(num)
            if len(result)==k:
                return result