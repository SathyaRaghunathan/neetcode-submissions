class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hm_s,hm_t = {},{}
        for i in range(len(s)):
            hm_s[s[i]] = hm_s.get(s[i],0) +1
            hm_t[t[i]] = hm_t.get(t[i],0) +1
        return hm_s==hm_t