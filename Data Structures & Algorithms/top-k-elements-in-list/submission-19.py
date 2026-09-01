class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = 1 + hm.get(num,0)

        count = [[] for i in range(len(nums)+1) ]
        
        for num, cnt in hm.items():
            count[cnt].append(num)

        result = []
        for i in range(len(count)-1,-1,-1):
            for val in count[i]:
                result.append(val)
                if len(result) == k:
                    return result


        