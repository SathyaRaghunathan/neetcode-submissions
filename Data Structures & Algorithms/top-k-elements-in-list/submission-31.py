class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort using count as ind
        hm = {}
        for num in nums:
            hm[num] = 1 +hm.get(num,0)
        
        buck = [[] for i in range(len(nums)+1)]
        for num,cnt in hm.items():
            buck[cnt].append(num)
        
        result = []
        for i in range(len(buck)-1,-1,-1):
            for num in buck[i]:
                result.append(num)
                if len(result)==k:
                    return result
        return