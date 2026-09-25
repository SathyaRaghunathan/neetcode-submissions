class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hm = defaultdict(int)
        t_hm = defaultdict(int)
        for char in s:
            s_hm[char]+=1
        for char in t:
            t_hm[char]+=1
        return s_hm==t_hm