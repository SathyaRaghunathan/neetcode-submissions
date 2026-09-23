class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0, len(height)-1
        l_max = [0]* len(height)
        r_max = [0]* len(height)
        #left to right
        l_max[0] = height[0]
        for i in range(1,len(height)):
            l_max[i] = max(l_max[i-1],height[i])
        
        r_max[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            r_max[i] = max(r_max[i+1],height[i])
        for i in range(len(height)):
            res += min(l_max[i],r_max[i])-height[i]
        return res
