class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute force with sorting
        if len(s)!= len(t):
            return False
        return sorted(s) == sorted(t)
        