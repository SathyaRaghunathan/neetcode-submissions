class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        result = [[] for i in range(len(nums)+1) ]
        for num in nums:
            hm[num] = 1 + hm.get(num,0)
        for num,cnt in hm.items():
            result[cnt].append(num)
        
        output = []
        for i in range(len(result)-1,-1,-1):
            for val in result[i]:
                output.append(val)
                if len(output) == k:
                    return output