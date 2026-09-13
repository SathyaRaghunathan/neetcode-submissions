class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        
        h1 = []
        for num,cnt in hm.items():
            heapq.heappush(h1,(cnt,num))
            if len(h1)>k:
                heapq.heappop(h1)
        result = []
        for i in range(k):
            result.append(heapq.heappop(h1)[1])

        return result