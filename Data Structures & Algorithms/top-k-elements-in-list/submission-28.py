class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm1 = defaultdict(int)
        for num in nums:
            hm1[num]+=1
        stack = []
        for num,cnt in hm1.items():
            stack.append([cnt,num])
        stack.sort()
        result = []
        while len(result)<k:
            result.append(stack.pop()[1])
        return result
