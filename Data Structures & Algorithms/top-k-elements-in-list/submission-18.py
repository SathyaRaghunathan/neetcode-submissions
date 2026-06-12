class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        hm = defaultdict(int)
        buck = [[] for i in range(len(nums)+1)]
        for num in nums:
            hm[num]+=1
        for key,val in hm.items():
            buck[val].append(key)
        output = []
        for i in range(len(buck)-1,0,-1):
            for num in buck[i]:
                output.append(num)
                if len(output)==k:
                    return output
        