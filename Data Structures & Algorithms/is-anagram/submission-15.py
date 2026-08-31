class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #naive solution
        s_sorted,t_sorted = sorted(s),sorted(t)
        return s_sorted == t_sorted

        