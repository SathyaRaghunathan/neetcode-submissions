class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        
        heap = []
        for num,count in hm.items():
            heapq.heappush(heap,(count,num))
            if len(heap)>k:
                heapq.heappop(heap)
        result = []

        for i in range(len(heap)):
            result.append(heapq.heappop(heap)[1])
        return result