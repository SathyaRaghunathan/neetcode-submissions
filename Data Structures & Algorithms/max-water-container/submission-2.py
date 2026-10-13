class Solution:
    def maxArea(self, heights: List[int]) -> int:
        abs_max = 0
        l,r = 0,len(heights)-1
        while l<r:
            loc_max = (r-l) * min(heights[l],heights[r])
            abs_max = max(loc_max,abs_max)
            if heights[l]< heights[r]:
                l+=1
            else:
                r-=1
        return abs_max