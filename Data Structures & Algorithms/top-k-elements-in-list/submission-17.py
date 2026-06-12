class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        hm = defaultdict(int)
        bucket = [[] for i in range(len(nums)+1)]
        for num in nums:
            hm[num]+=1
        for key,val in hm.items():
            bucket[val].append(key)
        
        output = []
        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                output.append(num)
                if len(output)==k:
                    return output