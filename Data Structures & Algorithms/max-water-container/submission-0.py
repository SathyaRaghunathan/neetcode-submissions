class Solution:
    def maxArea(self, heights: List[int]) -> int:
        abs_max = 0
        l,r = 0, len(heights)-1
        while l<r:
            lcl_max = (r-l) * min(heights[l],heights[r])
            abs_max = max(abs_max,lcl_max)
            if heights[l]<=heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
        return abs_max