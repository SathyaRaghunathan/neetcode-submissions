class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #solved using min heap
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        
        heap1 = []
        for num in hm.keys():
            heapq.heappush(heap1,(hm[num],num))
            if len(heap1)>k:
                heapq.heappop(heap1)

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap1)[1])
        return output