class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hm = defaultdict(int)
        for i, num in enumerate(numbers):
            diff = target -num
            if diff in hm:
                return [hm[diff]+1,i+1]
            hm[num] = i
        return