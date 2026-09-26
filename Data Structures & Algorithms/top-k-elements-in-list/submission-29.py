class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #go through nums, put the number in a hm
        #with the count being the value
        #sort the hashmap by the values
        #return the top k keys
        hm = defaultdict(int)
        for num in nums:
            hm[num]+=1
        hms = dict(sorted(hm.items(),key =lambda x:x[1],reverse =True))
        result = []
        for key in hms.keys():
            result.append(key)
            if len(result) ==k:
                return result